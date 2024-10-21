'''B) Write a python script to define a class student having members roll no, name, age, 
gender. Create a subclass called Test with member marks of 3 subjects. Create three 
objects of the Test class and display all the details of the student with total marks.
'''
class student:
    def __init__(self):
        self.rno=int(input("Enter Rno : "))
        self.name=input("Enter Name : ")
        self.age=int(input("Enter Age : "))
        self.gender=input("Enter Gender : ")

class test(student):
    def mark(self):
        self.m1=int(input("Enter M1 Marks : "))
        self.m2=int(input("Enter M2 Marks : "))
        self.m3=int(input("Enter M3 Marks : "))
        self.total=self.m1 + self.m2 + self.m3
    def dis(self):
        print("Rno : ",self.rno)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        print("Total Marks : ",self.total)
        
ob=test()
ob.mark()

ob1=test()
ob1.mark()

ob2=test()
ob2.mark()

ob.dis()
ob1.dis()
ob2.dis()