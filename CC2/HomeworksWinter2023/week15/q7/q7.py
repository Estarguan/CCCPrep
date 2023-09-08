import sys
input = sys.stdin.readline 
from bisect import bisect_left

n,k,q = map(int,input().strip().split())
a = list(map(int,input().strip().split()))
psa = [0]
dict = {}
for i in range(len(a)):
    psa.append(psa[-1]+a[i])
    if a[i] not in dict:
       dict[a[i]] = []
    dict[a[i]].append(i+1)
for i in range(q):
    a,b,x,y = map(int,input().strip().split())
    placea, placeb = -1,-1
    if a in dict and b in dict:
        placea = bisect_left(dict[a],x)
        placeb = bisect_left(dict[b],x)
    if placea != -1 and placea != len(dict[a]) and x <= dict[a][placea] <= y and placeb != -1 and placeb != len(dict[b]) and x <= dict[b][placeb] <= y and psa[y] - psa[x-1] > k:
      print("Yes")
    else:
      print("No")

    