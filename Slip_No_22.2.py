#B) Write a python script to implement bubble sort using list 
list=[2,6,9,1,0,3,7,9,8,60,4]
n=len(list)

for i in range(0,n-1):
    for j in range(0,n-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
            
print(list)