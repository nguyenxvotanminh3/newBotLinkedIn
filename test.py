hold = ["minh","man","nguyen"]
a="test"
b="test"
c="test"

hold.clear()
for i in range(0,1):
    hold.insert(i,a)
for i in range(1,2):
    hold.insert(i,b)
for i in range(2,3):
    hold.insert(i,c)



for i in range(len(hold)):
    print(hold[i])