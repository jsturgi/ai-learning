"""
Day 2: Matrix2D Implementation from Scratch
Goal: Understand matrices as transformations
"""

import math
from typing import List
from vector import Vector


class Matrix2D:
    """
    Matrix2D class representing linear transformations.

    A Matrix2D is viewed geometrically as a transformation that maps vectors
    to new vectors. Each column represents where the basis vectors land
    after the transformation.

    Attributes:
        data: 2D list of numbers representing the Matrix2D
        rows: Number of rows in the Matrix2D
        cols: Number of columns in the Matrix2D

    Example:
        >>> M = Matrix2D([[2, 0], [0, 3]])  # Scaling transformation
        >>> v = Vector([1, 1])
        >>> result = M.multiply_vector(v)  # Should give Vector([2, 3])
    """

    def __init__(self, data: List[List[float]]):
        """
        Initialize Matrix2D from 2D list.

        Args:
            data: 2D list where each inner list is a row
                  Example: [[1, 2], [3, 4]] represents a 2x2 Matrix2D
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __repr__(self) -> str:
        """
        Return string representation for debugging.

        Returns:
            String like "Matrix2D([[1, 2], [3, 4]])"
        """
        return f"Matrix2D({self.data})"

    def __str__(self) -> str:
        """
        Pretty print the Matrix2D in readable format.

        Returns:
            Multi-line string with formatted Matrix2D
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
        Apply this transformation to a vector (Matrix2D-vector multiplication).

        Geometric interpretation: Where does this vector land after
        the transformation represented by this Matrix2D?

        Mathematical: Each component of result is the dot product of
        a Matrix2D row with the input vector.

        Args:
            vector: The vector to transform

        Returns:
            Transformed vector

        Raises:
            ValueError: If Matrix2D columns don't match vector dimension

        Example:
            >>> M = Matrix2D([[2, 0], [0, 3]])  # Scale x by 2, y by 3
            >>> v = Vector([1, 1])
            >>> M.multiply_vector(v)  # Returns Vector([2, 3])
        """
        if self.cols != len(vector.components):
            raise ValueError(f"Matrix2D columns ({self.cols}) must match vector dimension ({len(vector.components)})")

        result = [vector.dot(Vector(row)) for row in self.data]
        return Vector(result)
    
    def multiply_Matrix2D(self, other: 'Matrix2D') -> 'Matrix2D':
        """ 
        Applies a transformation to the Matrix2D.

        Geometric interpretation: The returned Matrix2D represents a composed transformation
        that first applies other, then applies self.

        Mathematical: Each component of the Matrix2D is a dot product of the original Matrix2D's 
        rows and the transformation Matrix2D's columns.

        Order: Order matters here. self * other != other * self.

        Raises: ValueError: If Matrix2D Inner Dimensions don't match: mxn nxm works, nxm nxm does not.

        Example:
            >>> R = Matrix2D.rotation(90)
            >>> S = Matrix2D.scaling(2,1)
            >>> R.multiply_Matrix2D(S) # scale then rotate
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
        return Matrix2D(toReturn)

    @staticmethod
    def rotation(angle_degrees: float) -> 'Matrix2D':
        """
        Create a 2D rotation Matrix2D (counterclockwise).

        Rotates vectors counterclockwise by the given angle.

        Args:
            angle_degrees: Rotation angle in degrees

        Returns:
            2x2 rotation Matrix2D

        Mathematical formula:
            [cos(θ)  -sin(θ)]
            [sin(θ)   cos(θ)]

        Example:
            >>> R = Matrix2D.rotation(90)  # 90 degree rotation
            >>> v = Vector([1, 0])  # Unit vector along x-axis
            >>> R.multiply_vector(v)  # Should give approximately [0, 1]
        """
        radians = math.radians(angle_degrees)
        r1 = [math.cos(radians), -math.sin(radians)]
        r2 = [math.sin(radians), math.cos(radians)]

        return Matrix2D([r1, r2])

    @staticmethod
    def scaling(sx: float, sy: float) -> 'Matrix2D':
        """
        Create a 2D scaling Matrix2D.

        Scales x-coordinates by sx and y-coordinates by sy.

        Args:
            sx: Scale factor for x-direction
            sy: Scale factor for y-direction

        Returns:
            2x2 scaling Matrix2D

        Mathematical formula:
            [sx   0]
            [0   sy]

        Example:
            >>> S = Matrix2D.scaling(2, 3)
            >>> v = Vector([1, 1])
            >>> S.multiply_vector(v)  # Returns Vector([2, 3])
        """
        return Matrix2D([[sx, 0], [0, sy]])

    @staticmethod
    def shear(shear_factor: float) -> 'Matrix2D':
        """
        Create a 2D shear Matrix2D.

        Shears the plane along the x-axis. Points move horizontally
        in proportion to their y-coordinate.

        Args:
            shear_factor: How much to shear

        Returns:
            2x2 shear Matrix2D

        Mathematical formula:
            [1  shear_factor]
            [0       1      ]

        Example:
            >>> Sh = Matrix2D.shear(1)
            >>> v = Vector([0, 1])  # Point at (0,1)
            >>> Sh.multiply_vector(v)  # Returns Vector([1, 1])
        """
        return Matrix2D([[1, shear_factor], [0, 1]])

def determinant_2x2(Matrix2D):
        """
        Calculate determinant of a 2x2 Matrix2D.

        Geometric Meaning: The determinant tells you how much the 
        transformation scales AREA. If det=2, areas double. If det=0.5,
        areas are halved. If det=0, space collapses to a line!

        Args:
            Matrix2D: 2x2

        Returns:
            Float representing the area scaling factor

        Formula:
            For Matrix2D [[a, b], [c,d]]:
            det = a*d - b*c
        Example:
            >>> M = Matrix2D.scaling(2, 3)  # Scale x by 2, y by 3
            >>> determinant_2x2(M)  # Returns 6
            # Areas are scaled by factor of 6!
        """
        a,b = Matrix2D.data[0]
        c,d = Matrix2D.data[1]

        return a*d - b*c
