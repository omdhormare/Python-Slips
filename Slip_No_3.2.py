'''B) Write a python script to define a class student having members roll no, name, age, 
gender. Create a subclass called Test with member marks of 3 subjects. Create three 
objects of the Test class and display all the details of the student with total marks.
'''
class student:
    def Accept(self):
        self.rno=int(input("Enter Roll No : "))
        self.name=input("Enter Name : ")
        self.age=input("Enter Age : ")
        self.gender=input("Enter Gender : ")
        
    def dis(self):
        print("\nRoll No : ",self.rno)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        

class Test(student):
    def AcceptS(self):
        self.java=int(input("Enter Java Marks : "))
        self.python=int(input("Enter Python Marks : "))
        self.oose=int(input("Enter OOSE Marks : "))
        
    def disT(self):
        print("\nJava Marks : ",self.java)
        print("Python Marks : ",self.python)
        print("OOSE Marks : ",self.oose)
        print("Total Marks : ",self.java+self.python+self.oose)
        
    
ob=Test()
ob.Accept()
ob.AcceptS()
ob.dis()
ob.disT()    