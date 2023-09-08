freq = {}
n = int(input())
for i in range(n):
    r = int(input())
    freq[r] = freq.get(r,0) + 1
maximum = max(freq.values())
secondmax = 0
for v  in freq.values():
    if secondmax < v and v < maximum:
        secondmax = v
maxlist,secondlist = [],[]

for k,v in freq.items():
    if v == maximum:
        maxlist.append(k)
    elif v == secondmax:
        secondlist.append(k)

ans = 0
if len(maxlist) >= 2:
    print(abs(max(maxlist)-min(maxlist)))
else:
    print(max(max(maxlist)-min(secondlist),max(secondlist)-min(maxlist)))