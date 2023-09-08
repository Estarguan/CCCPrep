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
