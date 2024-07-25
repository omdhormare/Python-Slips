#A) Write a Python script using class to reverse a string word by word

class Rev():
    def __init__(self):
        self.s=input("Enter String : ")
        print(self.s[::-1])
        
        
ob=Rev()