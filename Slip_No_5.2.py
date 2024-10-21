#B) Write a python script to generate Fibonacci terms using generator function


def generate(n):
    a=0
    b=1
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
        
n=int(input("Enter Fibonacci Number : "))
print(list(generate(n)))