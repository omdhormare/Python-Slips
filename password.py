import random
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZzxcvbnmasdfghjklqwertyuiop"

length = 10
random_string = ''.join(random.sample(characters, length))

print(random_string)
