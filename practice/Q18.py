# 5 3 8     00 01 02   5 4 7
# 4 2 6     10 11 12   3 2 9
# 7 9 1     20 21 22   8 6 1
arr=[[5,3,8],
     [4,2,6],
     [7,9,1]]
arr1=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        arr1[i][j] = arr[j][i]
print(arr1)