bin=input("Enter a binary number with 8 digits:")
if (len(bin)!=8):
    print("The binary number is not valid, beacuse of wrong amount of digits")
else:
    sum=0
    for i in range(7):
        a=int(bin[i])
        if(a==1):
            sum += 1
    if(sum%2==int(bin[7])):
        print("Parity check ok")
    else:
        print("Parity check not good")
