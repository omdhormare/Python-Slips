#A) Write a Python program to unzip a list of tuples into individual lists
l=[(10,'a'),(30,'b'),(50,'c')]
print(list(zip(*l)))