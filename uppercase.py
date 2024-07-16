s="we are"
result=""
for i in range(len(s)):
  if(i==0 and s[i]!=" "):
    result+=s[i].upper()
  elif(s[i-1]==' ' and s[i]!=''):
    result+=s[i].upper()
  else:
    result+=s[i]
print(result)
