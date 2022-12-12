import sys
input = sys.stdin.readline

n = int(input())
obs={}
max = 0

for i in range(n):
    time,pos = map(int, input().split())
    obs[time] = pos
lst = sorted(obs)
for i in range(n-1):
    if abs(obs[lst[i+1]]-obs[lst[i]]) / abs(lst[i+1]-lst[i]) > max:
        max = abs(obs[lst[i+1]]-obs[lst[i]]) / abs(lst[i+1]-lst[i])
print(max)
