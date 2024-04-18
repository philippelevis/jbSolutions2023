fwd = []

def notfit(item, lst):
    for i in lst:
        if i*2 == item:
            return
    lst.append(item)
        

for i in range(1,51):
    notfit(i,fwd)
print(len(fwd))

bak = []
def notfit2(item,lst):
    if item*2 in lst:
        return
    else:
        lst.append(item)
for i in range(50,0,-1):
    notfit2(i,bak)

print(len(bak))
