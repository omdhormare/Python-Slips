'''B) Write a program to implement the concept of queue using list.'''
q=[]
ch=0

while ch!=4:
    ch=int(input("Enter A Choice : "))
    print("\n1.Insert \n2.Delete \n3.Display")
    if ch==1:
        n=int(input("Enter Number : "))
        q.append(n)
        print("Insert Number Succefully")
        
    elif ch==2:
        if len(q)==0:
            print("Queue Is Empty..")
        else:
            del q[0]
            print("Deleted Number : ",q)
            
    elif ch==3:
        print(q)