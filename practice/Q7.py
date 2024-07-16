# greatest common divisor
a=48
b=18
if a<b :
    c=a
else: c=b
for i in range(c+1,0,-1):
    if(a%i==0 and b%i==0):
        print(i, "is highest common divisor.")
        break
    
    
    
