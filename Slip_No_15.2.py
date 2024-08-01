''''B) Write a python program to accept string and remove the characters which have odd 
index values of given string using user defined function.'''

def odd_char():
    s=input("Enter String : ")
    for i in range(1,len(s),2):
        print(s[i],end="")
        
odd_char()