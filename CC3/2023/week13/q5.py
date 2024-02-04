def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def min_groups(n, m, friendships):
    parent = [i for i in range(n + 1)]
    rank = [1] * (n + 1)
    groups = n

    for _ in range(m):
        x, y = map(int, input().split())

        rootX = find(parent, x)
        rootY = find(parent, y)

        if rootX != rootY:
            union(parent, rank, rootX, rootY)
            groups -= 1

    return groups

# Example usage:
N, M = map(int, input().split())
friendship_list = [tuple(map(int, input().split())) for _ in range(M)]

result = min_groups(N, M, friendship_list)
print("Minimum number of groups:", result)
