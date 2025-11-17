import math
from typing import List, Union
from vector import Vector
from matrix import Matrix

class Matrix3D(Matrix):
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
        super().__init__(data)
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")
        if self.rows != 3:
            raise ValueError("Matrix must be 3D")
        

    def __repr__(self) -> str:
        """
        Return string representation for debugging.

        Returns:
            String like "Matrix3D([[1,2], [3,4])"
        """
        return f"Matrix3D({self.data})"

    @staticmethod
    def rotation(angle_degrees: float, axis: str) -> 'Matrix3D':
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
   

m = Matrix3D([[1,0,0], [0,2,0],[0,0,3]])
print(m)
col1 = m.get_column(0)
print(col1)
v = Vector([1,2,3])
m2 = m.multiply_vector(v)
print(m2)
m3 = m.__matmul__(m)
print(m3)
# Test rotation around z-axis by 90 degrees
# Should rotate (1, 0, 0) to approximately (0, 1, 0)
Rz = Matrix3D.rotation(90, "z")
v = Vector([1, 0, 0])
result = Rz.multiply_vector(v)
print(result)  # Should be approximately [0, 1, 0
Rx = Matrix3D.rotation(90, "x")
result = Rx.multiply_vector(v)
print(result)
Ry = Matrix3D.rotation(90, "y")
result = Ry.multiply_vector(v)
print(result)

# 3D scaling (what you originally wanted)
S3 = Matrix3D.scaling(2, 3, 4)
print(S3)
print()

# 4D scaling (just because you can!)
S4 = Matrix3D.scaling(2, 3, 4, 5)
print(S4)
print()

# Test it with a vector
v = Vector([1, 1, 1])
result = S3.multiply_vector(v)
print(result)  # Should be [2, 3, 4]



