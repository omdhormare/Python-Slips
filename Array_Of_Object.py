#Accept N student information for user use Array of objects
class student:
    def accept(self):
        self.rno=int(input("Enter Roll No : "))
        self.name=input("Enter Name : ")
        self.per=int(input("Enter Per : "))
    
    def dis(self):
        print("\nRoll No : ",self.rno)
        print("Name : ",self.name)
        print("Percentage : ",self.per)
    
ob=student()
a=[]
n=int(input("Enter Limit : "))
for i in range(0,n):
    ob.accept()
    a.append(ob)

for i in range(0,n):
    a[i].dis()