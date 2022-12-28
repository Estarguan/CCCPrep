import sys
input = sys.stdin.readline

n,d = map(int,input().strip().split())
if d != -1:
    ages = [22-d]
else:
    ages = []
for i in range(n):
    y, a = map(int,input().strip().split())
    if y <= 22:
        ages.append(a+(22-y))
    else:
        ages.append(a+22+(100-y))
ages = list(set(ages))
ages.sort()
diff1 = ages[1]-ages[0]
diff2 = ages[-1]-ages[-2]
if diff2>diff1:
    ages.pop()
else:
    ages.pop(0)
if d != -1:
    if d not in ages:
        ages.append(22-d)
        ages.pop(0)
        print(max(ages) - min(ages))
    else:
        print(ages[-1]-ages[0])
else:
    print(ages[-1] - ages[0])