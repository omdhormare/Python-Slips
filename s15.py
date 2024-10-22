'''A) Write a Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original and modified values 
of the said attributes.'''

class student:
    def accept(self):
        self.name = input("Enter Student Name : ")
        self.mark  = int(input("Enter Marks : "))
    def dis(self):
        print("\n Orignal Values : \n")
        print("Student Name : ",self.name)
        print("Student Name : ",self.mark)
    def modify(self):
        self.name=input("Enter Name To Modify : ")
        self.mark=int(input("Enter Marks To Modify : "))
    def Dis(self):
       print("\n Modify Values : ")
       print("\n Modify Name : ",self.name)
       print("\n Modify Marks : ",self.mark)

ob=student()
ob.accept()
ob.dis()
ob.modify()
ob.Dis()
       
        
        
class Student:
    # Constructor to initialize the student_name and marks attributes
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Create an object of the Student class with initial values
student = Student("Om", 85)

# Print the original attribute values
print("Original values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)

# Modify the attribute values
student.student_name = "Rahul"
student.marks = 92

# Print the modified attribute values
print("\nModified values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)
