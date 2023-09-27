import sys
input = sys.stdin.readline

<<<<<<< HEAD
n,m,r,c = map(int,input().split())
grid = [['a' for i in range(m)]for i in range(n)]
if r == n and c != m and c != 0:
  print("IMPOSSIBLE")
  sys.exit()
elif c == m and r != n and r != 0:
  print("IMPOSSIBLE")
  sys.exit()

for i in range(r,n):
  grid[i][-1] = chr(ord(grid[i][0])+1)
for i in range(c,m):
  grid[n-1][i]= chr(ord(grid[0][i])+1)
if r != n and c == 0:
  grid[-1][-1] = chr(ord(grid[-1][-1])+1)


for i in grid:
  print("".join(i))
=======
def checkRow(i):
    return a[i] == a[i][::-1]

def checkCol(i):
    l = 0
    r = n-1
    while l < r:
        if a[l][i] != a[r][i]: return False
        l,r = l+1, r-1
    return True

def bad():
    print("IMPOSSIBLE")
    sys.exit()

n,m,r,c = map(int, input().split())
a = [['a']*m for i in range(n)]
for i in range(r, n):
    a[i][-1] = chr(ord(a[i][0]) + 1)
for j in range(c, m):
    a[n-1][j] = chr(ord(a[-1][j]) + 1)
if r != n and c == 0:
    a[n-1][m-1] = 'c'

if r == n and c != m:
    if m%2 == 0 and c%2 != 0: bad()
    for i in range(m):
        if i < c//2 or i >= m - c//2: a[n-1][i] = a[0][i]
        else: a[n-1][i] = chr(ord(a[0][i]) + 1)
    if c%2: a[n-1][m//2] = a[0][m//2]
if c == m and r != n:
    if n % 2 == 0 and r % 2 != 0: bad()
    for i in range(n):
        if i < r//2 or i >= n - r//2: a[i][m-1] = a[i][0]
        else: a[i][m-1] = chr(ord(a[i][0]) + 1)
    if r % 2: a[n//2][m-1] = a[n//2][0]

rows, cols = 0, 0
for i in range(n):
    rows += checkRow(i)
for j in range(m):
    cols += checkCol(j)

if rows != r or cols != c:
    bad()
else:
    for x in a:
        print("".join(x))
>>>>>>> a4675a80e3dd06888fba356c0b2a52efe29a5f7d
