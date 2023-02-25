t = input()
grid = [[1,2],[3,4]]
for i in t:
    if i == "H":
        grid[0], grid[1] = grid[1], grid[0]
    if i == "V":
        grid[0][0],grid[0][1] = grid[0][1],grid[0][0]
        grid[1][0],grid[1][1] = grid[1][1], grid[1][0]
print(" ".join(map(str, grid[0])))
print(" ".join(map(str, grid[1])))
