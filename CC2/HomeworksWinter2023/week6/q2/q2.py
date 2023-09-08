n = int(input())
seen1 = set()
seen2 = set()
triangles = []
triangles.append(list(map(int,input().split())))
triangles.append(list(map(int,input().split())))
side_touch = 0
for i in range(n):
  cur = 0
  if triangles[cur][i] == 1:
    seen1.add(i)
    if i != n-1:
      if triangles[cur][i+1] == 1:
        if i+1 not in seen1:
          seen1.add(i+1)
          side_touch += 1
    if (i+1) % 2 == 1:
      if triangles[cur+1][i] == 1:
        if i not in seen2:
          seen2.add(i)
          side_touch += 1
        if i != n-1:
          if triangles[cur+1][i+1] == 1:
            if i+1 not in seen2:
              seen2.add(i+1)
              side_touch += 1
        if i != 0:
          if triangles[cur+1][i-1] == 1:
              side_touch += 1
for i in range(n):
  cur = 1
  if triangles[cur][i] == 1:
    seen2.add(i)
    if i != n-1:
      if triangles[cur][i+1] == 1:
        if i+1 not in seen2:
          seen2.add(i+1)
          side_touch += 1
print(len(seen1)*3+len(seen2)*3-side_touch*2)
