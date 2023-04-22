import sys
input = sys.stdin.readline
import math
from bisect import bisect_left,bisect_right

n,q = map(int,input().strip().split())
distances = []
for i in range(n):
    x,y= map(int,input().strip().split())
    
    distances.append(math.sqrt(x**2+y**2))
distances.sort()
for i in range(q):
    j = int(input())
    print(bisect_right(distances,j))