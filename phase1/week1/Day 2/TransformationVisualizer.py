"""
Transformation Visualizer
Visualizes how matrices transform the 2D plane.
"""

import numpy as np
import matplotlib.pyplot as plt
from matrix import Matrix
from vector import Vector


def plot_transformation(matrix, title: str = "Transformation") -> None:
    """
    Visualize how a matrix transforms the 2D plane.

    Shows side-by-side comparison of:
     - Original 2D grid and basis vectors (i-hat, j-hat)
     - Transformed grid and basis vectors after applying matrix

    This helps build geometric intuition for what matrices actually do
    to the space. Watch how the grid lines bend, stretch, or rotate.

    Args:
        matrix: Matrix object to visualize
        title: Description of the transformation

    Visual Elements:
        - Blue grid lines show how space is warped
        - Red arrow (i-hat): x-axis basis vector [1,0]
        - Green arrow (j-hat): y-axis basis vector [0,1]

    Example Usage:
        >>> M = Matrix.scaling(2, 0.5)
        >>> plot_transformation(M, "Scaling (2x, 0.5y)")
        # Shows original square grid stretched horizontally, compressed vertically
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

    # Create grid points
    x_points = np.linspace(-2, 2, 9)
    y_points = np.linspace(-2, 2, 9)

    # Plot original grid on ax1
    for x in x_points:
        ax1.plot([x, x], [y_points[0], y_points[-1]], 'b-', linewidth=0.5)
    for y in y_points:
        ax1.plot([x_points[0], x_points[-1]], [y, y], 'b-', linewidth=0.5)

    # Plot basis vectors on ax1 (original)
    ax1.arrow(0, 0, 1, 0, head_width=0.1, head_length=0.1, fc='red', ec='red', label='i-hat')
    ax1.arrow(0, 0, 0, 1, head_width=0.1, head_length=0.1, fc='green', ec='green', label='j-hat')
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Original')
    ax1.legend()

    # Plot transformed grid on ax2
    for x in x_points:
        # Transform vertical line
        points = np.array([[x, y] for y in y_points])
        transformed = np.array([matrix.multiply_vector(Vector(p)).components for p in points])
        ax2.plot(transformed[:, 0], transformed[:, 1], 'b-', linewidth=0.5)

    for y in y_points:
        # Transform horizontal line
        points = np.array([[x, y] for x in x_points])
        transformed = np.array([matrix.multiply_vector(Vector(p)).components for p in points])
        ax2.plot(transformed[:, 0], transformed[:, 1], 'b-', linewidth=0.5)

    # Plot transformed basis vectors
    i_hat = matrix.multiply_vector(Vector([1, 0])).components
    j_hat = matrix.multiply_vector(Vector([0, 1])).components
    ax2.arrow(0, 0, i_hat[0], i_hat[1], head_width=0.1, head_length=0.1, fc='red', ec='red', label='i-hat')
    ax2.arrow(0, 0, j_hat[0], j_hat[1], head_width=0.1, head_length=0.1, fc='green', ec='green', label='j-hat')
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.set_title(f'After {title}')
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Test 1: Scaling transformation
    print("Test 1: Scaling Transformation (2x, 0.5y)")
    M = Matrix.scaling(2, 0.5)
    plot_transformation(M, "Scaling (2x, 0.5y)")

    # Test 2: Rotation transformation
    print("\nTest 2: Rotation 45 degrees")
    R = Matrix.rotation(45)
    plot_transformation(R, "Rotation 45°")

    # Test 3: Rotation 90 degrees
    print("\nTest 3: Rotation 90 degrees")
    R90 = Matrix.rotation(90)
    plot_transformation(R90, "Rotation 90°")

    # Test 4: Shear transformation
    print("\nTest 4: Shear Transformation")
    Sh = Matrix.shear(1)
    plot_transformation(Sh, "Shear (factor=1)")

    # Test 5: Custom transformation
    print("\nTest 5: Custom Transformation")
    Custom = Matrix([[1, 1], [0, 1]])
    plot_transformation(Custom, "Custom Matrix [[1,1],[0,1]]")

    # Test 6: Reflection across y-axis
    print("\nTest 6: Reflection across y-axis")
    Reflect = Matrix([[-1, 0], [0, 1]])
    plot_transformation(Reflect, "Reflection (y-axis)")
