import sys
input = sys.stdin.readline

N,D = map(int,input().strip().split())
trol = list(map(int,input().strip().split()))
psa = [trol[0]]
for i in range(1,len(trol)):
  psa.append(psa[i-1]+trol[i])

for _ in range(D):
  n = int(input())
  F = psa[n-1]
  S = psa[-1]-psa[n-1]
  if F >= S:
    trol = trol[n:]
    print(F)
    psa = [trol[0]]
    for i in range(1,len(trol)):
      psa.append(psa[i-1]+trol[i])
  else:
    trol = trol[:n]
    print(S)
    psa = [trol[0]]
    for i in range(1,len(trol)):
      psa.append(psa[i-1]+trol[i])