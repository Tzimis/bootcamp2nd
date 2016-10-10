number=input("Enter number sequense:")
s=0
if(len(number)%2==0):
    for i in range(0,len(number),2):
        s+=int(number[i])*int(number[i+1])
else:
    for i in range(1,len(number),2):
        s+=int(number[i])*int(number[i-1])
    s = s+int(number[i+1])
print(s)
    
    
