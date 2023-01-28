n = int(input())

dsa = []
for i in range(n-1):
  l,r = map(int,input().split())
  if r > len(dsa):
    for _ in range(r-len(dsa)):
      dsa.append(0)
  dsa[l-1] += 1
  dsa[r-1] -= 1
psa = [dsa[0]]
for i in range(1,len(dsa)):
  psa.append(psa[i-1]+dsa[i])
print(max(psa))
