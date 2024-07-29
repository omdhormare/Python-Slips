'''A) Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area and Perimeter'''
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def length(self):
        print("Area of Rectangle : ",self.l*self.w)
    
    def perimeter(self):
        print("Area of Perimeter : ",2*(self.l*self.w))
    
    
l=float(input("Enter Rectangle Legth : "))
w=float(input("Enter Rectangle Width : "))

ob=Rectangle(l,w)
ob.length()
ob.perimeter()
