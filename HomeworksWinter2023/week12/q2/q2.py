n,m = map(int,input().split())
grid = [[False]*n for i in range(n)]
unreachable = set()
for i in range(m):
    y,x = map(int,input().split())
    y-=1
    x-=1
    #vertical
    for j in range(n):
        unreachable.add((x,i))
    #horizontal right
    for j in range(n):
        unreachable.add((i,y))
    tempx,tempy = x+1,y+1
    while tempx != n and tempy != n:
        unreachable.add((tempx,tempy))
        tempx += 1
        tempy += 1
    tempx,tempy = x-1,y-1
    while tempx != -1 and tempy != -1:
        unreachable.add((tempx,tempy))
        tempx -=1
        tempy -=1
    tempx,tempy = x-1,y+1
    while tempx != -1 and tempy != n:
        unreachable.add((tempx,tempy))
        tempx -= 1
        tempy += 1
    tempx, tempy = x+1,y-1
    while tempx != n and tempy != -1:
        unreachable.add((tempx,tempy))
        tempx += 1
        tempy -= 1
    for i in range(n):
        print(grid[i])
    print(unreachable)
    print(n*n-len(unreachable))