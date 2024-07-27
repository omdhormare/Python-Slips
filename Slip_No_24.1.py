'''A) Write a Python Program to Check if given number is prime or not. Also find 
factorial of the given no using user defined function'''
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c == 2:
        print("prime No ..")
    else:
        print("Not Prime No ..")

def factorial(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    print("Factorial No : ",f) 

     
n=int(input("Enter No : "))
prime(n)
factorial(n)
