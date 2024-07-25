#A) Write a python script to find the repeated items of a tuple

t=(10,20,10,50,60,20)

for i in t:
    if t.count(i)>1:
        print(i,end=" ")