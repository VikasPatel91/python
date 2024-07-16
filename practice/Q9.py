string ="amoubcu"
num=0
call=set(string)
call_len=len(call)
string_len=len(string)
if(call_len==string_len):
    print("There is no same alphabets in string.")
else:
    for i in range(len(string)):
        for j in range(i+1,len(string)):
          if string[i] in string[j]:
            print(string[i+1])
            num+=1
            break
          if(num==1):
            break

