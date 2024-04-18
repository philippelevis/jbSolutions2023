n = 20
string = 'VPVVPVVPPVPVVPPPPPVV'
pcount = 0
vcount = 0

pwins = 0
vwins = 0

for i in string:
    if i == "V":
        vcount += 1
    if i == "P":
        pcount += 1
    if pcount == 5:
        pwins += 1
        pcount, vcount = 0,0
    if vcount == 5:
        vwins += 1
        pcount, vcount = 0,0
    

print(pwins,vwins)
print(pcount,vcount)