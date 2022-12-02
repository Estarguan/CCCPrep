import sys
input = sys.stdin.readline

t = str(input().strip())
s = str(input().strip())

ans = "no"
for i in range(len(s)):
    if s in t:
        ans = "yes"
    s = s[1:] + s[0]
print(ans)
