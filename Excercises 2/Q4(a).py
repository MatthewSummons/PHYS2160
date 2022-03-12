# Q4(a).py
# Classes representing 2D & 3D Vectors
# Created by Shaheer Ziya on UTC+08 15:09

import math
class Vec2D:
    """Class Representing 2D Vectors"""

    def __init__(self, xCord, yCord) -> None:
        """Initialize Vector with x,y co-ordinates.
        Elements are assumed to be contained in the set of all real numbers."""
        self.x = xCord
        self.y = yCord
    

    def __str__(self: "Vec2D") -> str:
        return f"({self.x}, {self.y})^T"


    def __add__ (self: "Vec2D", other: "Vec2D") -> "Vec2D":
        "Return the elementwise sum of two 2D vectors"
        return Vec2D(
            (self.x + other.x),
            (self.y + other.y)
        )
    
    def __sub__(self: "Vec2D", other: "Vec2D") -> "Vec2D":
        "Return the elementwise subtaction of two 2D vectors : Self - Other"
        return Vec2D(
            (self.x - other.y),
            (self.y - other.y)
        ) 
    

    def __mul__(self: "Vec2D", other: "Vec2D") -> float:
        "Return the dot product of two 2D vectors"
        return (self.x * other.x) + (self.y * other.y)
    

    def __eq__(self: "Vec2D", other: "Vec2D") -> bool:
        "Check if two 2D vectors are equivalent"
        return (
            math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
        )
    

    # def __neq__(self: "Vec2D", other: "Vec2D") -> bool:
    #   """Check if two 2D vectors are unequal"""  
    #   return not (self.__eq__(other))
    

    def __abs__(self: "Vec2D") -> float:
        "Return the Euclidean Norm of the vector"
        return math.sqrt( (self.x * self.x) + (self.y * self.y) )