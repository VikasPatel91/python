arr=[43,24,45,15,78,33]
for i in range(len(arr)-1):
    if(arr[i]>arr[i+1] ):
        print("It is not monotonically increasing")
        break
    if(i==len(arr)-2):
        print("It is monotonically increasing")