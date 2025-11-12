"""
Day 2: Matrix Implementation from Scratch
Goal: Understand matrices as transformations
"""

import math
from typing import List
from vector import Vector


class Matrix:
    """
    Matrix class representing linear transformations.

    A matrix is viewed geometrically as a transformation that maps vectors
    to new vectors. Each column represents where the basis vectors land
    after the transformation.

    Attributes:
        data: 2D list of numbers representing the matrix
        rows: Number of rows in the matrix
        cols: Number of columns in the matrix

    Example:
        >>> M = Matrix([[2, 0], [0, 3]])  # Scaling transformation
        >>> v = Vector([1, 1])
        >>> result = M.multiply_vector(v)  # Should give Vector([2, 3])
    """

    def __init__(self, data: List[List[float]]):
        """
        Initialize matrix from 2D list.

        Args:
            data: 2D list where each inner list is a row
                  Example: [[1, 2], [3, 4]] represents a 2x2 matrix
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __repr__(self) -> str:
        """
        Return string representation for debugging.

        Returns:
            String like "Matrix([[1, 2], [3, 4]])"
        """
        return f"Matrix({self.data})"

    def __str__(self) -> str:
        """
        Pretty print the matrix in readable format.

        Returns:
            Multi-line string with formatted matrix
            Example:
                [1.00, 2.00]
                [3.00, 4.00]
        """
        rowstrings = []
        for row in self.data:
            rstring = ", ".join(f"{num:.2f}" for num in row)
            rowstrings.append(f"[{rstring}]")

        return "\n".join(rowstrings)

    def get_column(self, col_index: int) -> Vector:
        """
        Extract a column as a Vector.

        Geometric meaning: The i-th column shows where the i-th basis
        vector lands after this transformation.

        Args:
            col_index: Which column to extract (0-indexed)

        Returns:
            Vector containing the column values
        """
        column = [row[col_index] for row in self.data]
        return Vector(column)

    def multiply_vector(self, vector: Vector) -> Vector:
        """
        Apply this transformation to a vector (matrix-vector multiplication).

        Geometric interpretation: Where does this vector land after
        the transformation represented by this matrix?

        Mathematical: Each component of result is the dot product of
        a matrix row with the input vector.

        Args:
            vector: The vector to transform

        Returns:
            Transformed vector

        Raises:
            ValueError: If matrix columns don't match vector dimension

        Example:
            >>> M = Matrix([[2, 0], [0, 3]])  # Scale x by 2, y by 3
            >>> v = Vector([1, 1])
            >>> M.multiply_vector(v)  # Returns Vector([2, 3])
        """
        if self.cols != len(vector.components):
            raise ValueError(f"Matrix columns ({self.cols}) must match vector dimension ({len(vector.components)})")

        result = [vector.dot(Vector(row)) for row in self.data]
        return Vector(result)
    
    def multiply_matrix(self, other: 'Matrix') -> 'Matrix':
        """ 
        Applies a transformation to the matrix.

        Geometric interpretation: The returned matrix represents a composed transformation
        that first applies other, then applies self.

        Mathematical: Each component of the Matrix is a dot product of the original matrix's 
        rows and the transformation matrix's columns.

        Order: Order matters here. self * other != other * self.

        Raises: ValueError: If Matrix Inner Dimensions don't match: mxn nxm works, nxm nxm does not.

        Example:
            >>> R = Matrix.rotation(90)
            >>> S = Matrix.scaling(2,1)
            >>> R.multiply_matrix(S) # scale then rotate
            >>> returns [[0, -1], [2, 0]]

        """
        if (self.cols != other.rows):
            raise ValueError("Inner dimensions don't match")
        product = []
        for i in range(other.cols):
            product.append(self.multiply_vector(Vector(other.get_column(i))).components)
        toReturn = []
        for row_index in range(len(product[0])):
            new_row = []
            for column in product:
                new_row.append(column[row_index])
            toReturn.append(new_row)
        return Matrix(toReturn)

    @staticmethod
    def rotation(angle_degrees: float) -> 'Matrix':
        """
        Create a 2D rotation matrix (counterclockwise).

        Rotates vectors counterclockwise by the given angle.

        Args:
            angle_degrees: Rotation angle in degrees

        Returns:
            2x2 rotation matrix

        Mathematical formula:
            [cos(θ)  -sin(θ)]
            [sin(θ)   cos(θ)]

        Example:
            >>> R = Matrix.rotation(90)  # 90 degree rotation
            >>> v = Vector([1, 0])  # Unit vector along x-axis
            >>> R.multiply_vector(v)  # Should give approximately [0, 1]
        """
        radians = math.radians(angle_degrees)
        r1 = [math.cos(radians), -math.sin(radians)]
        r2 = [math.sin(radians), math.cos(radians)]

        return Matrix([r1, r2])

    @staticmethod
    def scaling(sx: float, sy: float) -> 'Matrix':
        """
        Create a 2D scaling matrix.

        Scales x-coordinates by sx and y-coordinates by sy.

        Args:
            sx: Scale factor for x-direction
            sy: Scale factor for y-direction

        Returns:
            2x2 scaling matrix

        Mathematical formula:
            [sx   0]
            [0   sy]

        Example:
            >>> S = Matrix.scaling(2, 3)
            >>> v = Vector([1, 1])
            >>> S.multiply_vector(v)  # Returns Vector([2, 3])
        """
        return Matrix([[sx, 0], [0, sy]])

    @staticmethod
    def shear(shear_factor: float) -> 'Matrix':
        """
        Create a 2D shear matrix.

        Shears the plane along the x-axis. Points move horizontally
        in proportion to their y-coordinate.

        Args:
            shear_factor: How much to shear

        Returns:
            2x2 shear matrix

        Mathematical formula:
            [1  shear_factor]
            [0       1      ]

        Example:
            >>> Sh = Matrix.shear(1)
            >>> v = Vector([0, 1])  # Point at (0,1)
            >>> Sh.multiply_vector(v)  # Returns Vector([1, 1])
        """
        return Matrix([[1, shear_factor], [0, 1]])
