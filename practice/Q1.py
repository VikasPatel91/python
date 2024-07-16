start=2
end=10
for i in range(start, end+1):
    for j in range(1,11):
        print(i,"*", j,"=",i*j,end=" ")  # same line
    print()