import sys
input = sys.stdin.readline 

t = int(input())

for i in range(t):
  a,b,n = map(int,input().split())
  i = 0
  while a*i <= n:
    if (n-a*i) % b == 0:
      print("YES")
      break
    i += 1
  else:
    print("NO")