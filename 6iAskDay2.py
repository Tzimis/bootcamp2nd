b=[]

for i in range(3):
    in_one=input("Enter a number with 1 digit:")
    if (len(in_one)!=1):
       print("The number is not valid, beacuse of wrong amount of digits")
       break
    else:
        b.append(in_one)
    in_two=input("Enter a number with 2 digits:")
    if (len(in_two)!=2):
       print("The number is not valid, beacuse of wrong amount of digits")
       break
    else:
        b.append(in_two)
    in_three=input("Enter a number with 3 digits:")
    if (len(in_three)!=3):
       print("The number is not valid, beacuse of wrong amount of digits")
       break
    else:
        b.append(in_three) 
   
print('  ',b[0],'|  ',b[3],'|  ',b[6],'\n')
print(' ',b[1],' |',b[4],' |',b[7],'\n')
print(b[2],'|',b[5],'|',b[8],'\n')
