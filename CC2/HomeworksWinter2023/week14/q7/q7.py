import sys
input = sys.stdin.readline

base = 'Good writing is good writing is good writing.'
pre, mid, suf = "Good writing is good ", " writing is good ", " is good writing."

def fun(lvl,idx):
    if lvl == 0: return base[idx]
    if idx < len(pre): return pre[idx]
    idx -= len(pre)
    if idx < l[lvl-1]: return fun(lvl-1,idx)
    idx -= l[lvl-1]
    if idx < len(mid): return mid[idx]
    idx -= len(mid)
    if idx < l[lvl-1]: return fun(lvl-1,idx)
    idx -= l[lvl-1]
    return suf[idx]

l = [0] * 31
l[0] = len(base)
for i in range(1, len(l)):
    l[i] = len(pre)+l[i-1]+len(mid)+l[i-1]+len(suf)

for _ in range(int(input())):
    n,k = map(int,input().split())
    print(fun(n,k-1)) if k <= l[n] else print('.')