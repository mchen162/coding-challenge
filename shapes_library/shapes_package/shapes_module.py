import math


class Circle:
    """
    This class implements the Circle API
    """
    def __init__(self, radius: float = None):
        #constructor/object--> stuff in the ()
        if radius < 0:
            raise ValueError("Supplied radius must be greater than 0")
            #raises is the same as "throw" in java --> used to throw an exception from a method or any block of code
        self.radius=radius
        
    def area(self):
        return round(math.pi*self.radius**2, 2)


class Rectangle:
    """
    This class implements the Rectangle API
    """
    def __init__(self, height: float = None, width: float = None):
        if height < 0 or width < 0:
            raise ValueError("Supplied width or height must be greater than 0")
        
        self.height=height
        self.width=width
        
    def area(self):
        return round(self.height*self.width, 2)


class RightTriangle:
    """
    This class implements the Right Triangle API
    """
    def __init__(self, height: float = None, width: float = None, hypotenuse: float = None):
        if height < 0 or width < 0 or hypotenuse < 0:
            raise ValueError("Supplied width, height, or hypotenuse must be greater than 0")
        
        self.height=height
        self.width=width
        self.hypotenuse=hypotenuse

    def pythagorean(self):
        theorem = self.height**2 + self.width**2 
        if theorem == self.hypotenuse**2:
            return True
        else:
            return False
            
    def area(self):
        return round(0.5*self.height*self.width, 2)

    
        