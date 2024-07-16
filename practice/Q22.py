a=[1,2,3,4,5,6,7]
for i in a:
   print(i,end=" ")
print()
length=len(a)
for i in range(2):
   new=a[length-1]
   for j in range(length-1,-1,-1):
      a[j]=a[j-1]
   a[0]=new

print(a)


























































