import math
from vector import Vector
class Vector3D(Vector):
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
        super().__init__(components)

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
v1 = Vector3D([1, 2, 3])
v2 = Vector3D([4, 5, 6])
print(v1 + v2)
print(v1.cross(Vector3D([0, 1, 0])))
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