tin=input("Enter Tax Identification Number:")
if (len(tin)!=9):
    print("Tax Identification Number not valid beacuse of wrong amount of digits")
else:
    check=int(tin[-1])
    sum=0
    for i in range(2,9):
        integerDigit=int(tin[-i])
        sum += integerDigit**(i-1)
    a=sum%11
    b=a%10
    print(a)
    if(check==b):
        print("Tax Identification Number valid")
    else:
        print("Tax Identification Number valid")
