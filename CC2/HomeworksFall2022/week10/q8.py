import sys
input = sys.stdin.readline

stk, ans, n = [0], 0, int(inpit())
for x in list(map, int(input().split())):
    while stk[-1] > x:
        stk.pop()
    if stk[-] < x:
        ans += 1
        stk.append(x)
print(ans)
