import sys
input = sys.stdin.readline
x,y,n = map(int,input().strip().split())
grid = [["."for x in range(x)] for y in range(y)]
for i in range(n):
    x1,y1,x2,y2 = map(int,input().strip().split())
    for y in range(y1-1,y2):
        for x in range(x1-1,x2):
            grid[y][x] = "X"
ans = 0
for i in grid:
    ans += i.count("X")
print(ans)
