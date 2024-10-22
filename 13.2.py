n=int(input("Enter Number : "))

try:
    if n>0:
        raise ValueError("+")
    else:
        raise ValueError("-")
except ValueError as e:
    print(e)
