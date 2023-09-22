import sys
input = sys.stdin.readline

c = int(input())
seen = [[0 for i in range(c)]for i in range(2)]


triangles = 0
rows = []
for i in range(2):
  rows.append(list(map(int,input().strip().split())))

shared = 0
for i in range(c):
  if rows[0][i] == 1:
    triangles += 1
  if i == c-1:
    if rows[0][i] == 1:
      if seen[0][i]:
        seen[0][i] = 1
      if (c-1)%2 == 0:
        if rows[1][i] == 1:
          if seen[1][i] == 0:
            seen[1][i] = 1
            shared += 1
    continue
  if i % 2 == 0:
    if rows[0][i] == 1:
      if seen[0][i] ==0:

        seen[0][i] = 1

      if rows[0][i+1] == 1:
        seen[0][i+1] = 1

        shared += 1

      if rows[1][i] == 1:
        seen[1][i] = 1

        shared += 1
  else:
    if rows[0][i] == 1:
      if seen[0][i] == 0:
        seen[0][i] =1

      if rows[0][i+1] == 1:
        seen[0][i+1] = 1

        shared += 1



for i in range(c):
  if rows[1][i]:
    triangles += 1
  if i == c-1:
    if rows[1][i] == 1:
      if seen[1][i] == 0:
        seen[1][i] = 1

    continue
  if rows[1][i] == 1:
    if seen[1][i] == 0:
      seen[1][i] = 1
    if rows[1][i+1] == 1:
      shared += 1
      seen[1][i+1] = 1



print(3*triangles-2*shared)


