string="we are not same"
length=len(string)
# for i in range(length-1,-1,-1):
#    print(string[i],end='')

arr=[]
word=""

for i in range(length):
   if(string[i]==' '):
      arr.append(word)
      word=""
   else:
      word+=string[i]
arr.append(word)

for i in range(len(arr)-1,-1,-1):
   print(arr[i],end=" ")