import sys
input = sys.stdin.readline 

word = input().strip()
R = int(input().strip())
C = int(input().strip())
g = [input().strip().split() for i in range(R)]
ways = 0
dir = [(-1, 0), (-1, 1),  (0, 1), (1, 1) , (1, 0) , (1, -1) , (0, -1), (-1, -1)]

def fun(r,c,k,idx,turn):
  global ways
  if idx == len(word):
    ways += 1
    return
  dr,dc = r+dir[k][0], c + dir[k][1]
  if 0 <= dr < R and 0 <= dc < C and g[dr][dc] == word[idx]:
    fun(dr,dc,k,idx+1,turn)
  if not turn:
    for dk in [(k+2)%8,(k-2+8)%8]:
      dr,dc = r+dir[dk][0],c+dir[dk][1]
      if 0 <= dr < R and 0 <= dc < C and g[dr][dc] == word[idx]:
            fun(dr,  dc, dk, idx+1, True)




for i in range(R):
  for j in range(C):
    if g[i][j] == word[0]:
      for k in range(8):
        dr = i+dir[k][0]
        dc = j + dir[k][1]
        if 0 <= dr < R and 0 <= dc < C and g[dr][dc] == word[1]:
          fun(dr,dc,k,2,False)
print(ways) 