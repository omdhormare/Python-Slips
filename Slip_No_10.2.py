'''B) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', 
'[' ']. These brackets must be close in the correct order. for example "()" and "()[]{}" are 
valid but "[)", "({[)]" and "{{{" are invalid.'''

class parantheses:
    def check(self):
        self.n=input("Enter Bracketes : ")
        self.p=['[]','()','{}']
        
        if self.n in self.p:
            print("Valid...")
        else:
            print("Invalid...")
            
ob=parantheses()
ob.check()