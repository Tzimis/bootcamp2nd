input_year=input("Enter year:")
y=int(input_year)
a=y%4
b=y%7
c=y%19
d=(19*c+15)%30
e=(2*a+4*b-d+34)%7
month=(d+e+114)//31
day=((d+e+114)%31)+14
if (day>30 and month%2==0 and month!=2 and month!=8):
    day=day%30
    month =month+1
elif(month==2 and day>28):
    a=y%4
    if (a%100!=0 or a%400==0):
        day=day%29
    else:
        day=day%28
    month =month+1    
elif(day>31):
    day=day%31
    month=month+1
print("Day:", day, "Month:", month )
