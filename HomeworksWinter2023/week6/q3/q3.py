import sys
input = sys.stdin.readline

word = input().strip()
R = int(input().strip())
C = int(input().strip())
g = [input().strip().split() for i in range(R)]
ways = 0
dir = [(-1, 0), (-1, 1),  (0, 1), (1, 1) , (1, 0) , (1, -1) , (0, -1), (-1, -1)]

def fun(r, c, k, idx, turn):
    global ways
    if idx == len(word):
        ways += 1
        return
    for i in range(k-2, k+3, 2):
        nk = (i+8) % 8
        nr, nc = r + dir[nk][0], c + dir[nk][1]
        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == word[idx] and (nk == k or not turn):
            fun(nr,  nc, nk, idx+1, (turn or nk != k))


for i in range(R):
    for j in range(C):
        if g[i][j] == word[0]:
            for k in range(8):
                ni, nj = i + dir[k][0], j + dir[k][1]
                if 0 <= ni < R and 0 <= nj < C and g[ni][nj] == word[1]:
                    fun(ni, nj, k, 2, False)
print(ways)
