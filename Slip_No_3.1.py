'''A) Write a Python program to check if a given key already exists in a dictionary. If 
key exists replace with another key/value pair.'''

d={"Rno": 1 , "Name" : "om" ,"per" : 96 , "address " : "pune"}

check=input("Enter Key To serch")

if check in d:
    print("Key Exists..")
    new_key=input("Enter New Key : ")
    new_value = input("Enter New Value : ")
    d[new_key]=new_value
    del d[check]
    
else:
    print("Not Found Key")
    
print("Update Dictonary : ",d)