import sys
input = sys.stdin.readline

p = float(input().strip())
y = int(input().strip())
n = int(input().strip())
year = int(input().strip())

for i in range(year-y):
    n += n*p/100
print(round(n))
