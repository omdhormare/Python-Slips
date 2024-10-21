def python():
    s=input("Enter String : ")
    upper=0
    lower=0
    
    for ch in s:
        if ch.isupper():
            upper = upper +1
        elif ch.islower():
            lower=lower + 1
        
    print("No Of Upper Case characters : ",upper)
    print("No Of Lower Case characters : ",lower)

python()