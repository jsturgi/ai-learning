class SVD:
    
    def __init__(self, n_components: int):
        """
        initialize svd object
        """
        self.n_components = n_components
        self.components_ = None # store V^T, shape (n_components, n_features)
        self.singular_values_ = None
        self.explained_variance_ = None
        self.mean_ = None
    
    def fit(self, X: np.ndarray):
        
        self.mean_ = X.mean(axis=0)
        centered_X = X - self.mean_
        At = centered_X @ centered_X.T
        eigenvalues, eigenvectors = np.linalg.eigh(At)
        idx = eigenvalues.argsort()[::-1] #indices to sort descending
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:,idx]
        #keep only top n_components
        eigenvalues = eigenvalues[:self.n_components] # transpose to match expected shape.
        eigenvectors = eigenvectors[:, :self.n_components]
        self.singular_values_ = np.sqrt(np.maximum(0, eigenvalues))
        self.components_ = (1/self.singular_values_)[:, None] * (eigenvectors.T @ centered_X)
        n_samples = X.shape[0]
        self.explained_variance_ = (self.singular_values_**2) / (n_samples - 1)

        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        X_centered = X - self.mean_
        return X_centered @ self.components_.T * (1/self.singular_values_)

    def inverse_transform(self, X_transformed: np.ndarray) -> np.ndarray:

        X_centered = (X_transformed * self.singular_values_) @ self.components_
        return X_centered + self.mean_
    
    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        
        return self.fit(X).transform(X)
