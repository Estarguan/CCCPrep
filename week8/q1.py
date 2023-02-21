import sys
input = sys.stdin.readline

d = {}
while True:
    num = input().strip()
    if num == "":
        break
    d[num] = d.get(num, 0) + 1

mode = 0
modes = []
for k,v in d.items():
    if v == mode:
        modes.append(k)
    elif v > mode:
        mode = v
        modes = [k]
modes.sort()
for i in modes:
    print(i)
