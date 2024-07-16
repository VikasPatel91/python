
s="""HackerRank.com presents "Pythonist 2"."""
string=""""""
for i in range(len(s)):
    if s[i].isupper():
        string+=(s[i].lower())
    elif s[i].islower():
        string+=(s[i].upper())
    else:
        string+=(s[i])
print(string)