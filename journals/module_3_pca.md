# Module 3 - Eigenvalues, Eigenvectors & PCA
**Date:** November 25, 2025

## What I Learned
- **Eigenvectors & Eigenvalues:**
    - Eigenvectors (`Av = λv`) are special directions that do not change direction during a linear transformation, only magnitude.
    - Eigenvalues (`λ`) represent the scaling factor along those eigenvectors.
    - In the context of PCA, eigenvectors of the covariance matrix point in the directions of maximum variance.
- **Principal Component Analysis (PCA):**
    - PCA is a method to find the "intrinsic dimensionality" of data by rotating the coordinate system to align with the directions of greatest variance.
    - The "best" fit line (PC1) minimizes the perpendicular distance (reconstruction error) from the data points.
    - **Spectral Theorem:** Guarantees that eigenvectors of symmetric matrices (like covariance matrices) are orthogonal. This is why PC1 is always perpendicular to PC2.
- **Data Shape vs. Dimensionality:**
    - PCA effectiveness is determined by the *shape* of the data (distribution of variance), not just the number of features.
    - Elliptical/plane-like data compresses well; circular/spherical data does not.
- **Law of Large Numbers:** Explained why random circular data results in a ~60/40 variance split instead of exactly 50/50 for small sample sizes.

## What I Built
- **Full PCA Implementation (from scratch):**
    - `fit(X)`: Centers data, computes covariance matrix, solves for eigenvalues/vectors.
    - `transform(X)`: Projects data onto the principal components (`X_centered @ components.T`).
    - `inverse_transform(X)`: Reconstructs data from reduced dimensions (lossy if k < n).
    - `fit_transform(X)`: Chained convenience method.
- **Math Library Enhancements:**
    - `determinant()`: Optimized using **Row Reduction** (Gaussian elimination) to achieve O(n³) complexity, replacing the O(n!) factorial cofactor expansion.
    - `Covariance Matrix` calculation.
- **Visualizations:**
    - 2D scatter plots showing original data with Principal Component arrows (scaled by `sqrt(eigenvalue)`).
    - 1D projection views showing data collapsed onto a line.
    - Reconstruction error visualization showing lines connecting original points to their projected location (visually confirming errors are perpendicular to PC1).
- **Extended Challenge 1 (Completed):**
    - Generated 3D plane-like data and visualized it using `mpl_toolkits.mplot3d`.
    - Verified "intrinsic dimensionality" predictions by observing variance distribution.
- **Extended Challenge 2 (Completed):**
    - Implemented **Whitening** (Sphering), transforming elliptical data into a circular distribution with unit variance in all directions.
    - Learned that whitening is essentially PCA + scaling by `1/sqrt(eigenvalue)`.
- **Extended Challenge 3 (Completed):**
    - Demonstrated PCA's failure on nonlinear data (concentric circles) where variance is balanced but structure exists.
    - Applied the **Kernel Trick** intuition by adding a computed feature (`radius = sqrt(x^2 + y^2)`), effectively mapping the data to 3D where the pattern became linear and separable by PCA.

## Key Breakthroughs & Insights
- **PCA's Linear Limitation:** PCA is fundamentally a *linear* method. It fails to capture nonlinear structures (like concentric circles or spirals) unless the data is mapped to a higher-dimensional space where those patterns become linear (the core concept behind Kernel PCA).
- **Whitening vs. Compression:** Realized the irony that while PCA seeks *unequal* variance for compression, Whitening seeks *equal* variance for preprocessing/decorrelation.
- **PCA as Intrinsic Dimensionality Detector:** PCA not only reduces dimensions but *discovers* the true underlying dimensionality of data, especially when high-dimensional data has hidden low-dimensional structure. Eigenvalues reveal how many dimensions truly matter.
- **Prediction Accuracy:** Successfully predicted the PCA behavior for plane-like 3D data (two significant PCs, one near-zero for noise) and other scenarios (elongated data leading to 90/10 split). This demonstrated a solid conceptual understanding.
- **Noise as a Feature:** Realized that small eigenvalues (like the 0.8% for PC3 in plane data) aren't "error" but represent meaningful variance, in this case, the deliberately added noise perpendicular to the plane.

## NumPy & Jupyter Skills Learned
- **3D Visualization:** Mastered `mpl_toolkits.mplot3d` for scatter plots, arrows (`quiver`), and view manipulation (`view_init`) to understand 3D geometry.
- **Jupyter Autocomplete:** Discovered efficient use of `Tab` for completions and `Shift+Tab` (once for signature, twice for full docs) for parameter inspection.
- **Tuple Unpacking:** Mastered `*` operator for unpacking tuples into function arguments (e.g., `np.random.uniform(*x_range)`).
- **Vectorized Operations:** Reinforced the efficiency and conciseness of NumPy's element-wise operations (`a*x + b*y`) over Python loops.
- **Array Stacking:** Utilized `np.column_stack` for combining 1D arrays into a 2D array.
- **Random Data Generation:** Proficiently used `np.random.uniform` and `np.random.normal` for creating diverse synthetic datasets.

## Mathematical Insights
- **Eigenvalue = Variance:** Validated that the eigenvalue associated with a principal component *exactly* equals the variance of the data projected onto that component.
- **Orthogonality:** Confirmed computationally that `PC1 · PC2 ≈ 0`, consistent with the Spectral Theorem.
- **Row Operations & Determinants:**
    - Adding a multiple of one row to another (Shear) preserves the determinant (volume).
    - Swapping rows flips the sign (orientation).
    - Scaling a row scales the determinant.
- **Projection as Coordinate Transformation:** `transform` doesn't move data; it finds the coordinates of the same data points in a new, rotated basis.

## Challenges
- **Geometric Intuition of Error:** It took time to visualize that reconstruction error is the *perpendicular* distance to the PC1 line. Seeing the "error lines" in the plot verified this.
- **Object vs. Data State:** Distinguishing between the PCA object (which holds the *rules* like `components_` and `mean_`) and the transformed data array (which is just numbers).
    - *Bug Fix:* Attempted to access `.mean_` on the transformed numpy array instead of the PCA object.
- **Visualization Complexity:**
    - *Arrow Placement:* Learned that `FancyArrowPatch` requires a vector start and end point, not just a length or single coordinate. Also realized arrows belong on the *original* data plot, not the transformed PC-space plot (where axes *are* the PCs).
    - *Subplots:* Managing `fig, axes = plt.subplots(...)` and indexing into `axes[i]` to build multi-panel visualizations.
- **Row vs. Column Indexing:** Confused accessing a full principal component row (`pca.components_[1]`) with accessing the second element of all components (`pca.components_[:, 1]`).

## Design Decisions
- **Method Chaining:** Implemented `fit()` to return `self`, allowing `fit_transform(X)` to be a clean one-liner: `return self.fit(X).transform(X)`. This mimics the elegant API design of libraries like scikit-learn.
- **Visualization Strategy:** Deliberately split testing into two phases:
    1. `n_components=2`: To visualize rotation without information loss.
    2. `n_components=1`: To visualize actual compression and reconstruction error.

## Code Quality
- **Architecture:** Refactored `Matrix` and `Vector` classes to support inheritance and cleaner separation of concerns.
- **Optimization:** Moved from naive determinant calculation to efficient row reduction.
- **Testing:** Verified implementation against known shapes (circles vs. ellipses) and manual variance calculations.

## Time Spent
~ 6.5 hours (Total across multiple sessions including theory, implementation, and challenges)
