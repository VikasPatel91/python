def make(a):
    def add(b):
        return a+b
    return add
x=make(5)
print(x(4))