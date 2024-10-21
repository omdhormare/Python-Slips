'''A) Write a python script to find the repeated items of a tuple'''

t=(100,200,300,400,500,600,500,400)

for i in t:
    if t.count(i)>1:
        print(i,end=" ")