"""n = int(input())
nums = list(map(int, input().split()))
ans = []

for a1 in range(1, n+1):
    used = [False]*(n+1)
    prev = a1

    works = True
    a = []
    for i in range(n-1):
        if prev <= 0 or prev > n or used[prev]:
            works = False
            break
        a.append(prev)
        used[prev] = True
        prev = nums[i]-prev
    if prev <= 0 or prev > n or used[prev]:
        works = False
    if works:
        print(*a, prev)
"""
#evans answer that i like

n = int(input())
a = list(map(int,input().split()))
b=[]
for i in range(1,a[0]+1):
    b.append([])
    b[-1].append(i)
    b[-1].append(a[0]-i)
    for i in range(1,n-1):
        b[-1].append(a[i]-b[-1][-1])
for i in range(n):
    if len(set(b[i])) != len(b[i]):
        continue
    else:
        for j in b[i]:
            if j < 0 or j > n:
                break
        else:
            print(" ".join(map(str,b[i])))
            break
