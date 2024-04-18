n = int(input())
a = [int(i) for i in input().split()]
a.sort()
if n < 4:
    print(-1)

def removeduplicate(data):
    countdict = {}
    for element in data:
        if element in countdict.keys():
             
            # increasing the count if the key(or element)
            # is already in the dictionary
            countdict[element] += 1
        else:
            # inserting the element as key  with count = 1
            countdict[element] = 1
    data.clear()
    for key in countdict.keys():
        data.append(key)

b = []
for i in range(1, len(a)-1):
    if a[i] == a[i+1] or a[i] == a[i-1]:
        b.append(a[i])

if len(a) > 1 and a[0] == a[1]:
    b.append(a[0])
if len(a) > 1 and a[-1] == a[-2]:
    b.append(a[-1])
b.sort()
c = b[:]
removeduplicate(c)
if n < 4:
    pass
elif len(c) == 0:
    print(-1)
elif len(c) == 1:
    print(c[-1]**2)
elif n > 4:
    print(c[-1]*c[-2])