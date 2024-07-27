'''
A) Write a python program to create a class Circle and Compute the Area and the 
circumferences of the circle.(use parameterized constructor)
'''
class circle:
    def __init__(self,r):
        self.r=r
    def Area(self):
        print("Area Of Circle : ",3.14*self.r*self.r)
    def circum(self):
        print("circumferences of circle : ",3.14*2*self.r)    
    
r=int(input("Enter Radius : "))    
ob=circle(r)
ob.Area()
ob.circum()