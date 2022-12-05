t, n = map(int, input().split())
cords=[0]
for i in range(n):
    cords.append(int(input()))
cords.sort(key = lambda v : -v if v < 0 else v)
cnt,cord = 0, 0
for i in range(1,n):
    t -= abs(cords[i]-cords[i-1])
    if (t >= 0):
        cnt += 1
    else:
        break
print(cnt)

""" my version
t, n = map(int, input().split())
cords=[]
for i in range(n):
    cords.append(int(input()))
abs_cords = list(map(abs, cords))
time,cnt,cord = 0, 0, 0
while time < t:
    s = abs_cords.index(min(abs_cords))
    if time + abs(cords[s]-cord) < t: #cord = 4 3 3-4 = -1
        time += abs(cords[s]-cord)
        cnt += 1
        cord = cords[s]
        cords.pop(s)
        abs_cords.pop(s)
    else:
        break
print(cnt)"""
