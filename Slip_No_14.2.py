'''B) Write a Python program to display plain text and cipher text using a Caesar 
encryption. '''

def enc():
    s=input("Entrer String : ")
    n=int(input("Enter Numnber : "))
    res=""
    
    for i in range(len(s)):
        ch=s[i]
        if ch.islower():
            res += chr((ord(ch)-97+n)%26+98)
        elif ch.isupper():
            res += chr((ord(ch)+65+n)%26+65)
        else:
            res += ch
    print(res)
    
enc()
