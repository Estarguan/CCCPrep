import sys
input = sys.stdin.readline

lst = []
for i in range(4):
    lst.append(list(map(int, input().split())))

num = sum(lst[0])
magic = True
for i in lst:
    if sum(i) != num:
        magic = False

count = 0
for x in range(4):
    for y in range(4):
         count += lst[y][x]
         if count == num:
             count = 0
if count > 0 or magic == False:
    print("not magic")
else:
    print("magic")
