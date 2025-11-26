import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Tuple
from matplotlib.patches import FancyArrowPatch

class PCA:
    """
    Principal Component Analysis (PCA) for dimensionality reduction.

    PCA finds the directions (principal components) in your data that
    have the most variance. These directions are eigenvectors of the
    covariance matrix. By projecting data onto the top few principal
    components, we can reduce the dimensions while keeping most of
    the information.

    The Algorithm:
    1. Center the data (subtract the mean)
    2. Compute the covariance matrix
    3. Find eigenvectors and eigenvalues of covariance matrix
    4. Sort eigenvectors by eigenvalue (largest first)
    5. Keep top k eigenvectors as principal components
    6. Project data onto these components

    Attributes:
        n_components: Number of principal components to keep
        components_: The principal components (eigenvectors)
        mean_: Mean of the training data
        explained_variance_: Variance explained by each component (eigenvalues)
        explained_variance_ratio_: Proportion of variance explained

    Example:
        >>> X = np.random.randn(100,50) # 100 samples, 50 features
        >>> pca = PCA(n_components=2)
        >>> X_reduced = pca.fit_transform(X) # Now (100, 2)
        >>> Print(f"Kept {pca.explained_variance_ratio_.sum():.1%} of variance")
    """
    def __init__(self, n_components: int = 2):
        """
        Initialize PCA.

        Args:
            n_components: Number of principal components to keep
        """
        self.n_components = n_components
        self.components_ = None
        self.mean_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None

    def fit(self, X: np.ndarray) -> 'PCA':
        """
        Fit PCA on data matrix X.

        This finds the principal components (directions of maximum
        variance) by computing eigenvectors of the covariance matrix.

        Args:
            X: Data matrix of shape (n_samples, n_features)

        Returns:
            self (for method chaining)
        
        Steps:
            1. Calculate the mean of each feature (column)
            2. Center the data by subtracting the mean
            3. Compute covariance matrix (X_Centered.T @  X_Centered) / (n-1)
            4. Compute eigenvectors and eigenvalues using np.linalg.eig()
            5. Sort eigenvectors by eigenvalue (descending)
            6. Store top n_components eigenvectors as components_
            7. Store corresponding eigenvalues as explained_variance_
            8. Calculate explained_variance_ratio_
        """
        self.mean_ = X.mean(axis=0)
        X_centered = X - self.mean_ #fit data onto mean
        cov_matrix = X_centered.T @ X_centered / X.shape[0]
        # use numpys optimized eigenvalue solver for symmetric matrices
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        #eigh returns eigenvalues in ascending order, we want descending.
        idx = eigenvalues.argsort()[::-1] #indices to sort descending
        eigenvalues = eigenvalues[idx]
        eigenvectorsd = eigenvectors[:,idx]
        #keep only top n_components
        eigenvalues = eigenvalues[:self.n_components] # transpose to match expected shape.
        self.explained_variance_ = np.array(eigenvalues) #get variance values from eigenvalues
        self.explained_variance_ratio_ = self.explained_variance_ / X_centered.var(axis=0).sum() #compute variance ratio
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Project data onto principal components.

        After fitting, this transforms data from original high-dimensional space to the
        lower-dimensional principal component space.

        Args:
            X: Data matrix of shape (n_samples, n_features)

        Returns:
            X_transformed = (X - mean) @ components.T

        This is a matrix multiplication where:
        - Each row of X is a data point
        - Each row of components is a principal component direction
        - Result: coordinates of each point in the PC space
        """
        X_centered = X - self.mean_ # align new data with training coordinate system
        X_transformed = X_centered@self.components_.T #project from high-dim space to low-dim PC space
        return X_transformed

    def fit_transform(self, X:np.ndarray) -> np.ndarray:
        """
        Fit PCA and transform in one step

        Args:
            X: Data matrix

        Returns:
            X_Transformed: Projected data
        """
        return self.fit(X).transform(X)

    def inverse_transform(self, X_transformed: np.ndarray) -> np.ndarray:
        """
        Transform data back to original space.

        This reconstructs the original data from the principal components.
        If n_components < n_features this is a lossy reconstruction.
        (you lose information from discarded components)

        Args:
            X_transformed: Data in PC space (n_samples, n_components)

        Returns: 
            X_reconstructed: Data in original space (n_samples, n_features)

        Mathematical Operation:
            X_reconstructed = X_transformed @ components + mean
        """
        X_centered = (X_transformed@self.components_) #un project the transformed data
        X_reconstructed = X_centered + self.mean_ #uncenter the data
        return X_reconstructed