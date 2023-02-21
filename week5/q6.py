import sys
input = sys.stdin.readline

N = int(input().strip())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))


if (table[0][0] < table[0][N-1]):
    j = 0
else:
    j = N-1

if (table[0][j] < table[N-1][j]):
    i = 0
else:
    i = N-1

if (i == 0 and j == 0):
    for x in range(N):
        for y in range(N):
            print(table[x][y], end = ' ')
        print('')

elif (i == 0 and j != 0):
    for x in range(N, 0, -1):
        for y in range(N):
             print(table[y][x-1], end= " ")
        print('')

elif (i > 0 and j > 0):
    for x in range(N, 0, -1):
        for y in range(N, 0, -1):
            print(table[x-1][y-1], end = " ")
        print('')
else:
    for x in range(N):
        for y in range(N, 0, -1):
            print(table[y-1][x], end = " ")
        print('')
