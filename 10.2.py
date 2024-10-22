class demo:
    def __init__(self):
        s=input("Enter Parantheses : ")
        l=['[]','{}','()']

        if s in l:
            print("valid Parantheses..")
        else:
            print("Invalid Paranthese")

ob=demo()
