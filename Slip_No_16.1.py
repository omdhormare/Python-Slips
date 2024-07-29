'''
A) Write a python script to create a class Rectangle with data member’s length, width 
and methods area, perimeter which can compute the area and perimeter of rectangle
'''
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
