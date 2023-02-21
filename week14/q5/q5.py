import sys
input = sys.stdin.readline

boxs = []
for i in range(int(input())):
    box.append(list(map(int,input().split())))

boxs.sort()
print(boxs)
items = []
for i in range(int(input())):
    items.append(list(map(int,input().split())))
items.sort(lambda x : x[0]*x[1]*x[2])