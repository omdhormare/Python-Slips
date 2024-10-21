''''B) Write a python program to accept string and remove the characters which have odd 
index values of given string using user defined function.'''

def string():
    s=input("Enter String  : ")
    for i in range(len(s)):
        if i%2==1:
            print(s[i],end="")

string()
    