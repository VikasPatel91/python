string="hello world"
word=""
vowel="aeiou"
for i in range(len(string)):
    if string[i] not in vowel:
         word+=string[i]
print("Resulting word:", word)