import math


class Vector:
    def __init__(self, components):
        self.components = components

    def __repr__(self):
        return f"Vector({self.components})"

    def __add__(self, other):
        """Add two vectors component-wise"""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)
    
    def __sub__(self, other):
        """
        Subtract two vectors component-wise
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors are of different dimension!")
        result = [a-b for a,b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, scalar):
        """Multiply vector by a scalar"""
        result = [scalar * component for component in self.components]
        return Vector(result)

    def magnitude(self):
        """Calculate the magnitude (length) of the vector"""
        sum_of_squares = sum(c**2 for c in self.components)
        return sum_of_squares ** 0.5

    def dot(self, other):
        """Compute dot product with another vector"""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))

    def normalize(self):
        """Return a unit vector (magnitude = 1) in the same direction"""
        return [component / self.magnitude() for component in self.components]

    def angle_between(self, other):
        """Calculate the angle between two vectors, return in degrees"""
        dot = self.dot(other)
        dot = dot / (self.magnitude() * other.magnitude())
        angle = math.degrees(math.acos(dot))
        return angle

    def projection(self, other):
        """Project self onto other"""
        # Get unit vector
        other_norm = other.normalize()
        unit = Vector(other_norm)
        # Get scalar by computing dot product of v1 (self) by normalized v2 (unit vector)
        scalar = self.dot(unit)
        proj_v = unit * scalar
        return proj_v
