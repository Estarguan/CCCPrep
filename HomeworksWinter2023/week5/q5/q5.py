import sys
input = sys.stdin.readline

n = int(input())
a, i = [0], 0
while True:
    if a[i]*10+2 > n:
        break
    a.append(a[i]*10+2)
    if a[i]*10+3 > n:
        break
    a.append(a[i]*10+3)
    i += 1
print(len(a)-1)
