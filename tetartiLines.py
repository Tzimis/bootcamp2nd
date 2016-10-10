
            
number=input("Enter a number with 9 digits:")
if (len(number)!=9):
    print("The number is not valid, beacuse of wrong amount of digits")
else:
    for i in range(3):
        print ((i%3)*' ',number[i],end='  ') 
        print(number[i+3],end='  ')
        print(number[i+6])
                
        
