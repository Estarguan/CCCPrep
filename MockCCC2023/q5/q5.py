n,m = map(int,input().split())
banned = []
for i in range(m):
    banned.append(int(input()))
routes = {}
for i in range(n):
    routes[i+1] = []
for i in range(n):
    line = list(map(int,(input().split())))
    routes[line[0]].append(line[1])
visited = [False for i in range(n+1)]
count = 0

def dfs(currentroute):
    for i in routes[currentroute]:

        if i in banned:
            continue
        if i != 727:
            if visited[i]:
                continue
            else:
                visited[i-1] = True
                count += 1
        else:
            if i == 727:
                count += 1
                visited[len(visited)-1] = True
                if count > ans:
                    return count

        dfs(i)
ans = dfs(1)
print(ans)