import math
from typing import List, Union
from Vector3D import Vector3D

class Matrix3D:
    """
    Matrix3D Class representing linear transformations.

    A matrix is viewed geometrically as a transformation that maps vectors 
    to new vectors. Each column represents where the basis vectors land
    after the transformation. Matrices should be 3D or higher and square.

    Attributes:
        data: 2D list of numbers representing the matrix
        rows: number of rows in the matrix
        cols: number of columns in the matrix
        
    Example:
        >>> M = Matrix3D([[2,0,0], [0,3,0], [0,0,5]]) # Scaling transformation
        >>> v = Vector3D([1,2,3])
        >>> result = M.multiply_vector(v) # should give Vector3D([2,6,15])
    """
    def __init__(self, data: List[List[float]]):
        """
        Initialize matrix from 2D list.

        Args:
            data: 2D list where each inner list is a row
                ex: [[1,2], [3,4]] represents a 2x2 matrix.
        """
        self.data = data
        self.rows = len(data) #counts number of inner lists (rows)
        self.cols = len(data[0]) if data else 0 # counts how many elements are in first row (columns). checks for empty matrix
        if (self.rows < 3 or self.cols < 3):
            raise ValueError("Matrix must at least be 3x3.")
        if (self.rows != self.cols):
            raise ValueError("Matrix not square")

    def __repr__(self) -> str:
        """
        Return string representation for debugging.

        Returns:
            String like "Matrix3D([[1,2], [3,4])"
        """
        return f"Matrix3D({self.data})"
    
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

    def multiply_vector(self, vector: Vector3D) -> Vector3D:
        """
        Apply this transformation to a vector (matrix-vector multiplication

        Geometric: Where does this vector land after the transformation 
        represented by this matrix?

        Math: Each component of result is a dot product of a matrix row
        with the input vector.

        Args:
            vector: Vector3D
        
        Returns:
            Vector3D
        
        Raises: ValueError: If matrix columns don't match vector dimension

        Example:
            >>>M = Matrix3D([[2,0, 0], [0,3, 0], [0,0,4)] #scale x by 2, y by 3, z by 4)
            >>>v = Vector3D([1,1,1]) # returns Vector3D([2,3,4])
        """
        if (len(vector.components) != self.cols):
            raise ValueError("Dimensions don't match columns")
        result = [vector.dot(Vector3D(row)) for row in self.data]
        return Vector3D(result)

    def multiply_matrix(self, other: 'Matrix3D') -> 'Matrix3D':
        """ 
        Applies a transformation to the matrix.

        Geometric interpretation: The returned matrix represents a composed transformation
        that first applies other, then applies self.

        Mathematical: Each component of the Matrix is a dot product of the original matrix's 
        rows and the transformation matrix's columns.

        Order: Order matters here. self * other != other * self.

        Raises: ValueError: If Matrix Inner Dimensions don't match: mxn nxm works, nxm nxm does not.

        """
        if (self.cols != other.rows):
            raise ValueError("Inner dimensions don't match")
        product = []
        for i in range(other.cols):
            product.append(self.multiply_vector(other.get_column(i)).components)
        toReturn = []
        for row_index in range(len(product[0])):
            new_row = []
            for column in product:
                new_row.append(column[row_index])
            toReturn.append(new_row)
        return Matrix3D(toReturn)
                
            
        

    @staticmethod
    def rotation(angle_degrees: float, axis: str) -> 'Matrix':
        """
        Create a 3D rotation matrix around the specified axis.

        Args:
            angle_degrees: Rotation angle in degrees
            axis: which axis to rotate around("x", "y", or "z")
        
        Returns:
            3x3 rotation matrix
        """
        radians = math.radians(angle_degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        negSin = -math.sin(radians)

        match axis:
            case "x":
                r1 = [1, 0, 0]
                r2 = [0, cos, negSin]
                r3 = [0, sin, cos]
            case "y":
                r1 = [cos, 0, sin] 
                r2 = [0, 1, 0]
                r3 = [negSin, 0, cos]
            case "z":
                r1 = [cos, negSin, 0]
                r2 = [sin, cos, 0]
                r3 = [0, 0, 1]
            case _:
                raise ValueError("Axis mismatch: Only x, y, or z is supported")
        return Matrix3D([r1,r2,r3])
                
        

        return Matrix([r1,r2])

    @staticmethod
    def scaling(*scales) -> 'Matrix3D':
        """
        Create a nD scaling matrix.

        Scales n coords by sn

        Args:
            *scales variable number of scale factors (one per dimension)

        Returns:
           nxn scaling matrix
        """
        n = len(scales)
        rows = []

        # [[scales[i] if i == j else 0 for j in range(n)]for i in range(n)] - nested list comprehension
        
        for i in range(n):
            row_n = []
            for j in range(n):
                if i == j: 
                    row_n.append(scales[i])
                else:
                    row_n.append(0)
            rows.append(row_n)
        return Matrix3D(rows)