# perfect number 6 = 1,2,3 
n=int(input())
check=0
for i in range(1,n):
    if(n%i==0):
     check+=i
if(n==check):
      print(n,"is Perfect number.")
else:
   print(n,"is not Perfect number.")