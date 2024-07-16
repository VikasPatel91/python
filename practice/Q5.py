def check(num):
    result=[]
    while(num>1):
       last=num%10
       num/=10
       result.append(int(last))

    start=0
    end=len(result)-1
    check=True
    while(start<end):
     if(result[start]!=result[end]):
        check=False
        break
     start+=1
     end-=1
     return check
n=1221
if(check(n)):
   print("This Number is palindrome.")
else:
   print("This Number is not palindrome.")