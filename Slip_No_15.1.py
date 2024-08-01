'''A) Write a Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original and modified values 
of the said attributes.'''

class student():
    def accept(self):
        self.name=input("Enter Student Name : ")
        self.mark=int(input("Enter Percentage : "))
        
    def dis(self):
        print("Original Values : ")
        print("Student Name : ",self.name)
        print("Student percentage : ",self.mark)
        
        print("\n Modify Values : ")
        self.name=input("Enter Modify Student Name : ")
        self.mark=int(input("Enter Modify Percentage : "))
        
        print("\n")
        
        print(" Modify Student Name : ",self.name)
        print("Modify Percentage : ",self.mark)

ob=student()
ob.accept()
ob.dis()