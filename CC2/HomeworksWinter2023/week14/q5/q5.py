import sys
from bisect import bisect_left, bisect_right
n,q = map(int,input().strip().strip().split())
stops = list(map(int,input().strip().split()))
stops.sort()
for i in range(q):
    L,R = map(int,input().strip().split())

    print(bisect_right(stops,R) - bisect_left(stops,L))