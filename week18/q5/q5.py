<<<<<<< HEAD
import sys
input = sys.stdin.readline

n,q = map(int,input().strip().split())
ep = list(map(int,input().strip().split()))
rating = [ep[0]]
for i in range(1,n):
  rating.append(ep[i] + rating[i-1])
for i in range(q):
  n1,n2 = map(int,input().strip().split())
  n1, n2 = n1-1, n2-1
  print(rating[-1]-(rating[n2]-rating[n1-1]) if n1 != 0 else rating[-1]-rating[n2])
=======
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
>>>>>>> 8c9766d (added most of the week 18 questions)
