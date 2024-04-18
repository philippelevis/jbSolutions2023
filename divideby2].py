a = int(input())
b = int(input())

def dividetillodd(num):
    i = num
    count = 0
    while i%2 == 0:
        print(i,end=' ')
        i = i//2
        print(i)
        count += 1
    print("count = ",count)
    return count

res = 0
compar = 0

for i in range(b,a,-1):
    if i%2 != 0:
        continue
    if dividetillodd(i) > compar:
        compar = dividetillodd(i)
        res = i
    else:
        continue

print(res)