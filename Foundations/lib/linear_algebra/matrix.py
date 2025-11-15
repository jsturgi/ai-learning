import math
from typing import List, Union
from Vector3D import Vector3D

class Matrix:
    """
    General-purpose Matrix class representing linear transformations in n-dimensional space.

    A matrix is viewed geometrically as a transformation that maps vectors to new vectors.
    Each column represents where the corresponding basis vector lands after the transformation.
    This class provides a flexible implementation for matrices of arbitrary dimensions.

    Attributes:
        data: 2D list of numbers representing the matrix, where each inner list is a row
        rows: Number of rows in the matrix
        cols: Number of columns in the matrix

    Mathematical Representation:
        A matrix M with dimensions m×n transforms vectors from n-dimensional space
        to m-dimensional space through matrix-vector multiplication.

    Example:
        >>> M = Matrix([[1, 2, 3], [4, 5, 6]])  # 2x3 matrix
        >>> # This matrix maps 3D vectors to 2D vectors
        >>> M.rows  # Returns 2
        >>> M.cols  # Returns 3

    Note:
        For specialized 2D and 3D operations with additional geometric methods
        (rotation, scaling, shear), see Matrix2D and Matrix3D classes.
    """

    def __init__(self, data):
        """
        Initialize matrix from nD list.

        Args:
            data: nD list where each inner list is a row
                ex: [[1,2], [3,4]] represents a 2x2 matrix.
        """
        for row in data:
            if len(row) != len(data[0]):
                raise ValueError("Jagged Array! All rows must be the same length.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    
    def __str__(self) -> str:
        """

        Pretty print the matrix in readable format.

        Returns:
         Multi-line string with formatted matrix
         Example:
             [1.00, 2.00, 3.00]
             [4.00, 5.00, 6.00]
        """
        rowstrings = []
        for row in self.data:
            rstring = ", ".join(f"{num:.2f}" for num in row)
            rowstrings.append(rstring)

        return "\n".join(rowstrings)
    
    def get_column(self, col_index: int) -> Vector3D:
        """
        Extract a column as a vector.

        Geometric: The i-th column shows where the i-th basis vector lands
        after this transformation.

        Args:
            col_index: Which column to extract (0-indexed)
        Returns:
            Vector3D containing the column values
        """
        column = [row[col_index] for row in self.data]
        return Vector3D(column)
    