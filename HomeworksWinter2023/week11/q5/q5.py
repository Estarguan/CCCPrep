import sys
input = sys.stdin.readline 

sz = int(1e5)
row,col,lft,rit = [0]*sz,[0]*sz,[0]*(2*sz-1),[0]*(2*sz-1)
n,k = map(int,input().split())
for i in range(n):
    r,c = map(int,input().split())
    r,c = r-1,c-1
    row[r] += 1
    col[c] += 1
    lft[r+c]+=1
    rit[r+sz-1-c] += 1
    if row[r] == k or col[c] == k or lft[r+c] == k or rit[r+sz-1-c] ==k:
        print(i+1)
        sys.exit(0)
print(-1)