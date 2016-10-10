inp=input("Enter Limit:")
n=int(inp)
s=0
a=[]
b=[]
i=1
while(i<n):
    if(i*(i+1)%2==0):
        s = i*(i+1)//2
    i += 1
    a.append(s)

for x in range(len(a)):
    y=len(a)
   
    while x<y-2:
       
       b.append(a[y-1]-a[x])
       y -= 1          
        

for i in b:
    if(i not in a):
        a.append(i)
a.sort()
a.remove(1)



o=0
while (o<len(a) and a[o]<=n):
    if (o%10!=9):
        print(a[o],end=',')
    else:
        print(a[o])
    o += 1

