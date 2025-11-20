import math
from typing import List, Union
from vector import Vector

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
    
    def __repr__(self) -> str:
        """
        Return string representation for debugging.

        Returns:
            String like "Matrix3D([[1,2], [3,4])"
        """
        return f"Matrix({self.data})"

    
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
    
    def get_column(self, col_index: int) -> Vector:
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
        return Vector(column)
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if (self.cols != other.cols or self.rows != other.rows):
            raise ValueError("Inner Dimensions don't match. Invalid operation")
        return Matrix([[x+y for x,y in zip(row_a, row_b)] for row_a,row_b in zip(self.data, other.data)])
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if (self.cols != other.cols or self.rows != other.rows):
            raise ValueError("Inner Dimensions don't match. Invalid operation")
        return Matrix([[x-y for x,y in zip(row_a, row_b)] for row_a,row_b in zip(self.data, other.data)])
    
    def __matmul__(self, other: 'Matrix') -> 'Matrix':
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
        return Matrix(toReturn)

    def multiply_vector(self, vector: Vector) -> Vector:
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
        result = [vector.dot(Vector(row)) for row in self.data]
        return Vector(result)
    
    def transpose(self) -> 'Matrix':
        result = []
        for i in range(self.cols):
            result.append(self.get_column(i).components)
        return Matrix(result)
    
    def power_iter(self, tolerance=0.00001, max_iter=1000, deflate_against=None):
        """
        Find the dominant eigenvalue and eigenvector using power iteration.

        Args:
            max_iter: Maximum number of iterations
            tolerance: Convergence threshold
        
        Returns:
            (eigenvalue, eigenvector) tuple
        """
        v = Vector.fill(self.cols, 1).normalize()

        for i in range(max_iter):
            new_v = self.multiply_vector(v)
            if deflate_against:
                for vec in deflate_against:
                    new_v = new_v -(new_v.projection(vec))
            new_v = new_v.normalize()
            if(new_v.dot(v) > 1 - tolerance):
                print(f"Converged in {i+1} iterations")
                v = new_v
                break
            v = new_v
        eval = v.dot(self.multiply_vector(v))
        return (eval, v)
    
    def find_top_k_eigenvalues(self, k, tolerance=0.01, max_iter=1000):
        eigenvalues = []
        eigenvectors = []

        for i in range(k):
            val, vec = self.power_iter(deflate_against=eigenvectors)
            eigenvalues.append(val)
            eigenvectors.append(vec)
        
        toReturn = list(zip(eigenvalues, eigenvectors))
        
        return toReturn
    
    def determinant(self):
        """
        Computes determinant
        """
        if self.cols != self.rows:
            raise ValueError("Not a square matrix. Determinant cannot be computed.")
        match self.rows:
            case 2:
                a,b = self.data[0]
                c,d = self.data[1]
                return a*d - b*c
            case 3:
                a,b,c = self.data[0]
                d,e,f = self.data[1]
                g,h,i = self.data[2]
                return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)


            




    
    @staticmethod
    def scaling(*scales) -> 'Matrix':
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
      for i in range(n):
          row_n=[]
          for j in range(n):
              if i == j:
                  row_n.append(scales[i])
              else:
                  row_n.append(0)
          rows.append(row_n)

      return Matrix(rows)
    
    @staticmethod
    def identity(size=3) -> 'Matrix':
        """
        Creates an identity matrix using the dimension passed.

        Args:
            Size: Int - sets the dimension of the Identity matrix
        
        Returns:
            Matrix - Identity Matrix
        """
        identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        return Matrix(identity)
