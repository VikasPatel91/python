# pyramid star pattern
k=0
for i in range(1, 8):
    k=k+1 if i<=4 else k-1
    for j in range(1,8):
        if(j>5-k and j<=3+k):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

