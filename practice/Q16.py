arr=[5,2,3,5,3,6]
for i in range(len(arr)):
    num=arr.count(arr[i])
    if (num==1):
        print(f"{arr[i]} is lonely number")
        num=0
    