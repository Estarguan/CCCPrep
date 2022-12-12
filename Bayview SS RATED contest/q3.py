n,m,k = map(int, input().split())
seats = []
ans = 0
for i in range(n):
    seats.append([False for _ in range(m)])

for i in range(k):
    x,y = map(int,input().split())
    seats[x-1][y-1] = True
for row in range(n):
    for col in range(m):
        if seats[row][col]:
            continue
        else:
            cnt = 0
            if row > 0 and seats[row-1][col]: cnt += 1 #pre row
            if row < n-1 and seats[row+1][col]: cnt += 1 # next row
            if col > 0 and seats[row][col-1]: cnt += 1 # pre col
            if col < m-1 and seats[row][col+1]:cnt += 1 # next col
            if row > 0 and col > 0 and seats[row - 1][col - 1]:  cnt += 1 # up left
            if row > 0 and col < m - 1 and seats[row-1][col+1]: cnt += 1 # up right
            if row < n-1 and col > 0 and seats[row+1][col-1]: cnt += 1 #down left
            if row < n-1 and col < m-1 and seats[row+1][col+1]: cnt += 1
            if cnt >= 3: ans += 1
print(ans)
