nums=[3,4,2,1]
target=6
arr1=[]
for i in range(0,len(nums)-1):
   for j in range(i+1,len(nums)):
      if(nums[i]+nums[j]==target):
         arr1.append(i)
         arr1.append(j)
print(arr1)