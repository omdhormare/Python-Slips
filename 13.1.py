n=int(input("Enter Number : "))

try:
    if n>0:
        raise ValueError("p")
    else:
        raise ValueError("N")
except ValueError as a:
    print(a)
