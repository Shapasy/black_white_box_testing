#--------------------------------------------------------------------------------------------
import unittest
#--------------------------------------------------------------------------------------------
from Shapes import Square,Rectangle
#--------------------------------------------------------------------------------------------
class TestSquare(unittest.TestCase):
    def testName(self):
        self.assertEqual(Square(2).getName(),"Square")

    def testArea(self):
        self.assertAlmostEqual(Square(5).getArea(),5**2)
        self.assertAlmostEqual(Square(7.2).getArea(),(7.2)**2)
        self.assertAlmostEqual(Square(0.5).getArea(),(0.5)**2)
        self.assertAlmostEqual(Square(0.231).getArea(),(0.231)**2)

        self.assertAlmostEqual(Square(0).getArea(),-1)
        self.assertAlmostEqual(Square(-5).getArea(),-1)
        self.assertAlmostEqual(Square(-8.23).getArea(),-1)
        self.assertAlmostEqual(Square(None).getArea(),-1)
        self.assertAlmostEqual(Square('ok').getArea(),-1)

    def testPerimeter(self):
        self.assertAlmostEqual(Square(5).getPerimeter(),5*4)
        self.assertAlmostEqual(Square(7.2).getPerimeter(),(7.2)*4)
        self.assertAlmostEqual(Square(0.5).getPerimeter(),(0.5)*4)
        self.assertAlmostEqual(Square(0.231).getPerimeter(),(0.231)*4)

        self.assertAlmostEqual(Square(0).getPerimeter(),-1)
        self.assertAlmostEqual(Square(-5).getPerimeter(),-1)
        self.assertAlmostEqual(Square(-8.23).getPerimeter(),-1)
        self.assertAlmostEqual(Square(None).getPerimeter(),-1)
        self.assertAlmostEqual(Square('hi').getPerimeter(),-1)
        
#--------------------------------------------------------------------------------------------
class TestRectangle(unittest.TestCase):
    def testName(self):
        self.assertEqual(Rectangle(8,12).getName(),"Rectangle")

    def testArea(self):
        self.assertAlmostEqual(Rectangle(5,2).getArea(),5*2)
        self.assertAlmostEqual(Rectangle(7.2,2).getArea(),(7.2)*2)
        self.assertAlmostEqual(Rectangle(0.5,0.2).getArea(),(0.5)*(0.2))
        self.assertAlmostEqual(Rectangle(0.231,0.3214).getArea(),(0.231)*(0.3214))

        self.assertAlmostEqual(Rectangle(0,2).getArea(),-1)
        self.assertAlmostEqual(Rectangle(-5,4).getArea(),-1)
        self.assertAlmostEqual(Rectangle(-8.23,-23.1).getArea(),-1)
        self.assertAlmostEqual(Rectangle(None,2).getArea(),-1)
        self.assertAlmostEqual(Rectangle(3,'hello').getArea(),-1)

    def testPerimeter(self):
        self.assertAlmostEqual(Rectangle(5,2).getPerimeter(),(5+2)*2)
        self.assertAlmostEqual(Rectangle(7.2,2).getPerimeter(),((7.2)+2)*2)
        self.assertAlmostEqual(Rectangle(0.5,0.2).getPerimeter(),((0.5)+(0.2))*2)
        self.assertAlmostEqual(Rectangle(0.231,0.3214).getPerimeter(),((0.231)+(0.3214))*2)

        self.assertAlmostEqual(Rectangle(0,2).getPerimeter(),-1)
        self.assertAlmostEqual(Rectangle(-5,4).getPerimeter(),-1)
        self.assertAlmostEqual(Rectangle(-8.23,-23.1).getPerimeter(),-1)
        self.assertAlmostEqual(Rectangle(5,None).getPerimeter(),-1)
        self.assertAlmostEqual(Rectangle('cat',9).getPerimeter(),-1)
#--------------------------------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
#--------------------------------------------------------------------------------------------