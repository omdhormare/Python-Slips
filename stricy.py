'''l=[]

def no():
    for i in range(1,11):
        l.append(i*i)
    
    return l

print(no())'''
n=int(input("Enter No :  "))
cout=0
for i in range(1,n+1):
    if n%i==0:
        cout=cout+1
if cout==2:
    print("Prime No : ")
else:
    print("Not Prime No ")