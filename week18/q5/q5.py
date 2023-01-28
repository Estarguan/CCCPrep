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
