import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(list(map(int,input().strip().split())))
ans = 0
while len(q) > 1:
    if q[0] == q[-1]:
        q.popleft()
        q.pop()
    elif q[0] > q[-1]:
        tmp = q.pop()
        q[-1] += tmp
        ans += 1
    elif q[0] < q[-1]:
        tmp = q.popleft()
        q[0] += tmp
        ans += 1
print(ans)
