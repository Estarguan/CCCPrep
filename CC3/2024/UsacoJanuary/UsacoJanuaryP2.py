import time
start_time = time.time()
#end_time = start_time + 4000
n, s = map(int, input().split())
points = {}
power = 1
targets = 0
dir = 1
broken = [False] * (n + 1)
count = 0
#visTimes = [0] * (n+1)


for i in range(1, n + 1):
    type, v = map(int, input().split())
    points[i] = [type, v]

while 1 <= s <= n:
    if time.time() - start_time > 3.7:
      break
    #visTimes[s] += 1
    #if visTimes[s] > 4000:
      #break
    if points[s][0] == 0:
        dir *= -1
        power += points[s][1]
    if points[s][0] == 1:
        if not broken[s] and power >= points[s][1]:  # Combined conditions
            targets += 1
            broken[s] = True
    s += dir * power

print(targets)