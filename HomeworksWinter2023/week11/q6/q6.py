import sys
input = sys.stdin.readline 

def fun():
    
    for j in range(n-1,-1,-1):
      for k in range(m):
          if grid[j][k] == 'X':
              grid[j][k] = '.'
          if j != 0:
            if grid[j-1][k] == 'X':
                grid[j][k] = 'X'
    for j in range(n):
        open=[]
        for k in range(m):
            if grid[j][k] == '.':
                open.append([j,k])
            if grid[j][k] == 'X':
                open = []
            if grid[j][k] == 'W':
                if len(open) != 0:
                    l,r = open.pop(0)
                    grid[l][r] = 'W'
                    grid[j][k] = '.'
    for j in range(n-1,-1,-1):
      
      for k in range(m):
          if grid[j][k] == 'X':
              continue
          if j != n-1:
              if grid[j+1][k] == 'X':
                  continue
          
          if j != 0:
            if grid[j-1][k] == 'W':
                if grid[j][k] != 'W':
                  grid[j][k] = 'W'
                  grid[j-1][k] = '.'
                
    for j in range(n):
          open=[]
          for k in range(m):
              if grid[j][k] == '.':
                  open.append([j,k])
              if grid[j][k] == 'X':
                  open = []
              if grid[j][k] == 'W':
                  if len(open) != 0:
                      l,r = open.pop(0)
                      grid[l][r] = 'W'
                      grid[j][k] = '.'
    
          
def output():
    for i in range(n):
        print(''.join(grid[i]))

n,m = map(int,input().strip().split())
grid = []
for i in range(n):
    grid.append(list(input().strip()))
q = int(input())
for i in range(q):
    t = int(input())
    if t == 1:
        fun()
    else:
        output()
        