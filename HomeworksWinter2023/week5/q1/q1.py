def infront(grid,i,j):
  if j != m-1:
    if grid[i][j+1] == ".":
      grid[i][j+1] = "C"
def behind(grid,i,j):
  if j != 0:
    if grid[i][j-1] == ".":
      grid[i][j-1] = "C"
def below(grid,i,j):
  if i != n-1:
    if grid[i+1][j] == ".":
        grid[i+1][j] = "C"
def above(grid,i,j):
  if i != 0:
    if grid[i-1][j] == ".":
      grid[i-1][j] = "C"
n,m = map(int,input().split())

grid = []
for i in range(n):
  grid.append(list(input()))
if n == 1 and m == 1:
  print(grid[0][0])
else:
  for i in range(n):
    for j in range(m):
      if grid[i][j] == "W":
        if n == 1:
          infront(grid,i,j)
          behind(grid,i,j)
        elif m == 1:
          above(grid,i,j)
          below(grid,i,j)
        else:
          if i == 0:
            infront(grid,i,j)
            behind(grid,i,j)
            below(grid,i,j)
          elif i == n-1:
            infront(grid,i,j)
            behind(grid,i,j)
            above(grid,i,j)
          else:
            infront(grid,i,j)
            behind(grid,i,j)
            below(grid,i,j)
            above(grid,i,j)
  for i in grid:
    print("".join(i))
