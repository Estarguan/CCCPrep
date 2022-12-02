import sys
input = sys.stdin.readline

order = {}
for i in range(int(input())):
    order[input().strip()] = []
for i in range(int(input())):
    order[input().strip()].append(i+1)

for i in order.values():
    for x in i:
        print(x)
