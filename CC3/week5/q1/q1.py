n = int(input())
speed = 0
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
data.sort(key = lambda x : x[0])
for i in range(len(data)-1):
    time = data[i+1][0]-data[i][0]
    dist = abs(data[i+1][1]-data[i][1])
    if dist/time > speed:
        speed = dist/time
print(speed)




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