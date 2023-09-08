import sys
input = sys.stdin.readline

N,D = map(int,input().strip().split())
trol = list(map(int,input().strip().split()))
psa = [0]
for i in range(N):
  psa.append(psa[i]+trol[i])

for _ in range(D):
  n = int(input())
  F = psa[:n+1]
  S = psa[n:]


  if F[-1]-F[0] >= S[-1]-S[0]:
    psa = S
    print(F[-1]-F[0])
    
  else:
    psa = F
    print(S[-1]-S[0])
