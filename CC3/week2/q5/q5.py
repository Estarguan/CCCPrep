import sys
from collections import deque
input = sys.stdin.readline

MM = int(2e5+2)
x,y = map(int, input().split())
dis = [0 for i in range(MM)]
vis = [False for i in range(MM)]
q = deque()

q.append(x)
vis[x] = 1
dis[x] = 0 
while q:
    cur = q.popleft()
    
    moves = [cur-1, cur+1, cur*2]
    for move in moves:
        if move == y:
            if dis[cur]+1 < dis[move]:
                dis[move] = dis[cur]+1
        if 0 < move < MM and not vis[move]:
            vis[move] = True
            dis[move] = dis[cur] + 1
            q.append(move)
print(dis[y])