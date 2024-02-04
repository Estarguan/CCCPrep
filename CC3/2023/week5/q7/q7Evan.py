import sys
input = sys.stdin.readline
from collections import deque

def walking():
    q = deque([start])
    vis = set()
    dist = {}
    dist[start] = 0
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        cur = q.popleft()
        if cur == end:
            return dist[cur]
        for ac,bc in dir:
            a,b = cur[0] + ac, cur[1] + bc
            if 0<=a<r and 0<=b<c and (a,b) not in vis:
                if graph[a][b] == "O":
                    q.append((a,b))
                    vis.add((a,b))
                    dist[(a,b)] = dist[cur] + 1

def teleportation():
    q = deque([start])
    vis = set()
    dist = {}
    dist[start] = 0
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        cur = q.popleft()
        if cur in portals:
            return dist[cur]
        for ac, bc in dir:
            a, b = cur[0] + ac, cur[1] + bc
            if 0 <= a < r and 0 <= b < c and (a, b) not in vis:
                if graph[a][b] == "O":
                    q.append((a, b))
                    vis.add((a, b))
                    dist[(a, b)] = dist[cur] + 1

r,c = map(int, input().split())

start = tuple(list(map(int, input().split())))
end = tuple(list(map(int, input().split())))
graph = []
for  in range(r):
    graph.append([*input()])
portals = set()
for  in range(int(input())):
    portal = tuple(list(map(int, input().split())))
    portals.add(portal)

print(walking()-teleportation())