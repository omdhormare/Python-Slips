'''A) Write a Python program to input a positive integer. Display correct message for 
correct and incorrect input. (Use Exception Handling)'''

try:
    n=int(input("Enter No : "))
    if n>0:
        print("Positive No ..")
    else:
        print("Incorrect...")
except:
    print("Incorrect Input...")