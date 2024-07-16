arr=[5,3,6,3,2]
arr.sort(reverse=True)
maxi=max(arr)
for i in range(len(arr)):
  if (maxi != arr[i]):
    print( arr[i])
