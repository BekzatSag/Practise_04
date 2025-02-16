from Square import Square
class Cube(Square):
    def __init__(self, side):
        Square.__init__(self, side)
        self.side = side
    def get_info():
        return "This class calculates surface area and volume of the cube"
    def __str__(self):
        return f"Cube with side {self.side} cm" 
    def get_surface_area(self):
        return self.side*self.side
    def get_volume(self):
        return self.side*self.side*self.side
print("Class Cube is imported successfully")