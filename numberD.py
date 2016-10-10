#3iAskisi
number=input("Enter a number with 10 digits:")
if (len(number)!=10):
    print("The number is not valid, beacuse of wrong amount of digits")
else:
    for i in range(10):
        adig=int(number[i])
        if (adig%2==1):
            print(adig,end=' ')
    print("\n")
    for i in range(10):
        adig=int(number[i])
        if (adig%2==0):
            print(' ',adig,end='')
