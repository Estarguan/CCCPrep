import sys
input = sys.stdin.readline

s,ex = input().strip(), input().strip()

stk = []
for c in s:
    stk.append(c)
    if len(stk) >= len(ex) and "".join(stk[len(stk) - len(ex):]) == ex:
        for i in range(len(ex)):
            stk.pop()
print("FRULA") if len(stk) == 0 else print("".join(stk))
