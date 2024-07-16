string="ABCDCDC"
sub_string="CDC"
s=[]
word=""
count=0
for i  in range(len(string)-2):
    for j  in range(i+0,len(sub_string)+i):
        word+=string[j]
    s.append(word)
    word=""
print(s)
print(s.count(sub_string))