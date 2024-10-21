'''A) Write a Python script using class, which has two methods get_String and 
print_String. get_String accept a string from the user and print_String print the string in 
upper case.'''

class demo:
    def get_string(self):
        self.s=input("Enter String : ")
    
    def print_string(self):
        print(self.s.upper())

ob=demo()
ob.get_string()
ob.print_string()