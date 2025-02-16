class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def get_info():
        return "This class calculates perimeter and area of the rectangles"
    def __str__(self):
        return f"Rectangle with width {self.w} cm and height {self.h} cm"
    def get_perimeter(self):
        return 2*(self.w + self.h)
    def get_area(self):
        return (self.w * self.h)
print("Class Rectangle is imported successfully")