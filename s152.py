'''B) Write a python program to accept string and remove the characters which have odd 
index values of given string using user defined function.'''

class string:
    s=input("Enter String : ")
    for i in range(1,len(s),3):
        print(s[i],end="")

string()
