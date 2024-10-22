l1=[]

n=int(input("Enter Limit : "))

for i in range(0,n):
    n1=int(input("Enter Number : "))
    l1.append(n1)

print("Remove Duplicate Number : ",list(set(l1)))
