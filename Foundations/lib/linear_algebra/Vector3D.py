import math
class Vector3D:
    """
    3D Vector class

    A 3D vector is viewed as a linear combination of
    basis vectors: x*i-hat +  y*j-hat + z*k-hat

    Attributes:
        data: [x,y,z]

    Example:
        >>> v = Vector3D([1,1,2])
    """
    def __init__(self, components):
        if (len(components)) != 3:
            raise ValueError("Must have exactly 3 components")
        self.components = components
        
    def __repr__(self):
        return f"Vector({self.components})"
        
    def __add__(self, other):
        """ Add two vectors component-wise"""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")
        result = [a+b for a,b in zip(self.components, other.components)]
        return Vector3D(result)
        
    def __mul__(self, scalar):
        """Multiply vector by a scalar"""
        result = [scalar * component for component in self.components]
        return Vector3D(result)
        
    def magnitude(self):
        """
        Compute the length of the vector.

        The magnitude of the vector determines the
        distance from the  origin.

        Returns:
            float: magnitude
        Formula:
            Pythagorean Theorem: square root(a**2 + b**2 + c**2)
        Example:
            >>> v = Vector3D([3, 4, 0])
            >>> v.magnitude()
            5.0
        """
        # use pythagorean theorem
        sum_of_squares = sum(c**2 for c in self.components)
        return sum_of_squares ** .5
        
    def dot(self, other):
        """
        Computes the dot product with another vector.

        The dot product is a measure of how aligned two vectors are.
        If dot = 0, the vectors are perpendicular, and the angle is 90 degrees. If > 0, the 
        vectors point in similar direction and the angle trends towards 0 degrees. If < 0, 
        the vectors point in  opposite directions and the angle trends towards 180 degrees.

        Args:
            other: Vector3D to compute dot product with
        
        Returns:
            Float Dot Product
        
        Formula:
            |a| * |b| * cos(θ), a1*b1 + ... + ax*bx

        Example:
            >>> v1 = Vector3D([1, 0, 0])
            >>> v2 = Vector3D([0, 1, 0])
            >>> v1.dot(v2)
            0  # Perpendicular vectors  
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")  
        return sum(a*b for a,b in zip(self.components, other.components))
        
    def normalize(self):
        """
        Maintains vector direction while reducing magnitude to one.

        Normalizing a vector transforms it into a unit vector. A unit
        vector represents pure direction and can be scaled into any
        magnitude.

        Formula:
            Each component / magnitude

        Use Cases:
            - Representing pure direction
            - Normalizing Data for ML algorithms
            - Lighting Calculation for Graphics/Game Engines
        
        Returns:
            Vector3D unit vector (magnitude = 1) in the same direction

        Example:
            >>> v = Vector3D([3, 4, 0])
            >>> v.normalize()
            Vector3D([0.6, 0.8, 0.0])  # magnitude = 1
        """
        return Vector3D([component / self.magnitude() for component in self.components])

    def cross(self, other):
        """
        Returns a vector normal to self and other.

        The cross product produces a new vector that is normal (perpendicular)
        to the plane formed by the two input vectors. The direction is determined
        by the right-hand rule - Index finger - self, Middle Finger - other, thumb - cross product This
        rule is anti-commutative - a*b = -(b*a). The magnitude of the cross product
        represents the area of the parallelogram formed by the two input vectors.

        Formula:
            x = a2*b3 -a3*b2
            y = a3*b1 - a1*b3
            z = a1*b2 - a2*b1

        Args:
            other: Vector3D

        Returns:
            Vector3D

        Example:
            >>> v1 = Vector3D([1,0,0])
            >>> v2 = Vector3D([0,1,0])
            v1.cross(v2) # [0,0,1]
            v2.cross(v1) # [0,0,-1]
        """
        x = (self.components[1]*other.components[2]) - (self.components[2]*other.components[1])
        y = (self.components[2]*other.components[0]) - (self.components[0]*other.components[2])
        z = (self.components[0]*other.components[1]) - (self.components[1]*other.components[0])

        return Vector3D([x,y,z])


# Cross Product Testing
v1,v2 = Vector3D([2,0,0]), Vector3D([0,3,0])
cross = v1.cross(v2)
print(cross)
if  ((cross.dot(v1) == 0) and (cross.dot(v2) == 0)):
    print("perpendicular!")
else:
    print("not perpendicular!")

v3, v4 = Vector3D([1,2,0]), Vector3D([0,1,3])
cross2 = v3.cross(v4)
print(cross2)
if  ((cross2.dot(v3) == 0) and (cross2.dot(v4) == 0)):
    print("perpendicular!")
else:
    print("not perpendicular!")

#parallel
v5,v6 = Vector3D([1,2,3]), Vector3D([2,4,6])
cross3 = v5.cross(v6)
print(cross3)
if  ((cross3.dot(v5) == 0) and (cross3.dot(v6) == 0)):
    print("perpendicular!")
else:
    print("not perpendicular!")