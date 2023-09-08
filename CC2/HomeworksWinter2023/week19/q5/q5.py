import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int,input().strip().split()))
dic = {}
mods = set()
for i in range(n):
  mods.add(arr[i]%k)
  if arr[i]%k not in dic:
    dic[arr[i]%k] = [arr[i]]
  else:
    dic[arr[i]%k].append(arr[i])
mods = list(mods)
mods.sort()
for i in mods:
  if len(dic[i]) > 1:
    for j in sorted(dic[i]):
      print(j,end=' ')
  else:
    print(dic[i][0], end=' ')