'''A) Write Python class to perform addition of two complex numbers using binary + 
operator overloading'''

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def __add__(self,other):
        real_sum=self.real + other.real
        img_sum=self.img + other.img
        print("Sum : ",real_sum,"+",img_sum,"i")
        
ob=complex(10,20)
ob1=complex(100,200)

ob+ob1