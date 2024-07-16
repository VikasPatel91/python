string=" my name is vikku i am from the village "
count=1
length=len(string)
for i in range(1,length-1):
    if (string[i] == ' ' ):
        count += 1
print(count)