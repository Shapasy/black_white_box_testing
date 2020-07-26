#--------------------------------------------------------------------------------------------
# OOP program that is calculate Area and Perimeter of different shapes.
#--------------------------------------------------------------------------------------------
from Shapes import Square,Rectangle
#--------------------------------------------------------------------------------------------
if __name__ == '__main__':
    square = Square(5)
    print("Square Area :",square.getArea())
    print("Square Perimeter :",square.getPerimeter())

    rectangle = Rectangle(2,3)
    print("Rectangle Area :",rectangle.getArea())
    print("Rectangle Perimeter :",rectangle.getPerimeter())
#--------------------------------------------------------------------------------------------







































