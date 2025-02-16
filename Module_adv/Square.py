from Rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side
    def __str__(self):
        return f"Square with side {self.side} cm"
print("Class Square is imported successfully")