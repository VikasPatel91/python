# f=open("f1","r")
with open("f1","r") as f:
    if "Twinkle" in f.read():
        print("available")
        
    else:
        print("not available")