n=int(input("Enter Number : "))

try:
    if n>0:
        raise ValueError("Positive Number..")
    else:
        raise ValueError("Nrgative Number..")
    
except ValueError as e:
    print(e)