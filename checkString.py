text= input()
if "yes" in text:
    is_spam=True
elif "me" in text:
    is_spam=True
else:
    is_spam=False

if is_spam :
    print("spam")
else:
    print("not spam")