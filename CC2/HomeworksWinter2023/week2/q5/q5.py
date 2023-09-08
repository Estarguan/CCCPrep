I = int(input())
N = int(input())
J = int(input())
count = 0
stat = [0 for i in range(I+1)]
for i in range(J):
  l,r,num = map(int,input().split())
  l, r = l-1, r-1
  stat[l] += num
  stat[r+1] -= num
psa = [stat[0]]
for i in range(1,len(stat)):
  psa.append(psa[i-1]+stat[i])
for i,v in enumerate(psa):
  if i == I:
    break
  if v < N:
    count += 1
print(count)
