import sys
input = sys.stdin.readline

grid = []
n,m = map(int,input().strip().split())
for i in range(n):
    grid.append(list(map(int,input().strip().split())))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            if i == 0 and j == 0:
                grid[i][j] = 1
            elif i == 0:
                grid[i][j] = grid[i][j-1] + 1
            elif j == 0:
                grid[i][j] = grid[i-1][j]+1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1]) + 1
        else:
            if i > 0 and grid[i][j] <= grid[i-1][j]:
                print(-1)
                sys.exit()
            elif j > 0 and grid[i][j] <= grid[i][j-1]:
                print(-1)
                sys.exit()
for i in range(n):
    print(" ".join(map(str,grid[i])))