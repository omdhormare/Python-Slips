'''A) Write Python class to perform addition of two complex numbers using binary + 
operator overloading'''

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def __add__(self,other):
        sum1=self.real + other.real
        sum2= self.img + other.img
        print(sum1, "+" ,sum2,"i")
    
ob=complex(100,200)
ob1=complex(200,300)

ob+ob1