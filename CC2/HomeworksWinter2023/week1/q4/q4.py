m = int(input())
n = int(input())
k = int(input())

paintRow = [False] * m
paintCol = [False] * n

for i in range(k):
    rc, pos = input().split()
    pos = int(pos) - 1

    if rc == "R":
        paintRow[pos] = not paintRow[pos]
    else:
        paintCol[pos] = not paintCol[pos]

gold = 0
black_rows = 0
gold_rows = 0


for i in range(m):
    if paintRow[i] == True:
        gold_rows += 1
        gold += n
    else:
        black_rows += 1

newGold = 0

for i in range(n):
    if paintCol[i] == True:
        newGold = black_rows - gold_rows
        gold += newGold

print(gold)
