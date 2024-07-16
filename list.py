# both homo and hetro data
l=[4,74,34]
l.append(5)
l.insert(3,3) # insert at a particular position
l.remove(4) # remove value
l.pop(2) # remove using index
l.sort()
# print(l.count(0)) # it count number of times values available in list
# print(max(l))
# print(min(l))
# l.clear() # clear full list
l.reverse()
print(l)

a=list(map(int,input().split())) # it is use to insert list when we give space in input
# input 4 2 4 2 output [4,2,4,2]
a=list(map(int,input().strip())) # it is use to insert list when we write multiple digits
# input 3422 output [3,4,2,2]
print(a)