import math
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,a,b,t = map(int,input().split())
    num = (t+b*n)/(a+b)
  
    if math.ceil(num) > n:
        print(-1)
    else:
        print(math.ceil(num))
  