'''B) Write a Python class which has two methods get_String and print_String. get_String 
accept a string from the user and print_String print the string in upper case. Further 
modify the program to reverse a string word by word and print it in lower case.'''

class python:
    def get_string(self):
        self.s=input("Enter String : ")
    def print_string(self):
        print("Upper Case : ",self.s.upper())
    def rev_lower(self):
        print("Reverse : ",self.s[::-1].lower())
        

ob=python()
ob.get_string()
ob.print_string()
ob.rev_lower()