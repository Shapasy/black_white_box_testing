#--------------------------------------------------------------------------------------------
# Parent Class (Shape)
class Shape:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name
        
    def getArea(self):
        pass

    def getPerimeter(self):
        pass
    
    def block(self,num):
        if(num <= 0): return True
        else: return False
#--------------------------------------------------------------------------------------------
# Child Class (Square)
class Square(Shape):
    def __init__(self,side):
        Shape.__init__(self,'Square')
        self.side = side

    def getArea(self):
        try:
            if(Shape.block(self,self.side)): return -1
            return self.side*self.side
        except: return -1
        
    def getPerimeter(self):
        try:
            if(Shape.block(self,self.side)): return -1
            return self.side*4
        except: return -1
#--------------------------------------------------------------------------------------------
# Child Class (Rectangle)
class Rectangle(Shape):
    def __init__(self,length,width):
        Shape.__init__(self,'Rectangle')
        self.length = length
        self.width = width

    def getArea(self):
        try:
            if(Shape.block(self,self.length) or Shape.block(self,self.width)): return -1
            return self.length*self.width
        except: return -1

    def getPerimeter(self):
        try:
            if(Shape.block(self,self.length) or Shape.block(self,self.width)): return -1
            return (self.length+self.width)*2
        except: return -1
#--------------------------------------------------------------------------------------------    