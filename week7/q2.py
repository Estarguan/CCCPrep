import sys
input = sys.stdin.readline

count = 0
for i in range(6):
    N = input().strip()
    if N == "W":
        count += 1
    if N == "L":
        pass
if count >= 5:
    print(1)
elif 3 <= count < 5:
    print(2)
elif 1 <= count < 3:
    print(3)
else:
    print(-1)
