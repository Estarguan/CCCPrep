import sys
input = sys.stdin.readline 

n = int(input())

flowers = list(map(int,input().strip().split()))
cnt = 0

for i in range(n):
  for j in range(i+1,n+1):

    if sum(flowers[i:j])/(j-i) in flowers[i:j]:
      cnt+= 1
print(cnt)