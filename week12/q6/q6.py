k,n = map(int, input().split())
ranks =[]
ans = [[0]*n for _ in range(n)]
finans = 0
for i in range(k):
    ranks.append(list(map(int, input().split())))



for x in range(k): #0
    for y in range(n): #0
        for z in range(y+1, n): #0
            temp = ranks[x][y]
            ans[temp-1][ranks[x][z]-1] += 1
for i in ans:
    finans += i.count(k)
print(finans)