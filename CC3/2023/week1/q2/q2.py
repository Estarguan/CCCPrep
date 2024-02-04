import sys
input = sys.stdin.readline 

n,m = map(int,input().strip().split())
for i in range(2,n+1):
  print(1,i)
  m -= 1

for i in range(2, n+1):
 if m > 0:
   for j in range(i+1,n+1):
     if m > 0:
       print(i,j)
       m-= 1



