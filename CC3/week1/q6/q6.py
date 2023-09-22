

tot, connect = 0, True
for i in range(4):
  row = 0
  lst = list(map(int,input().split()))
  tot += sum(lst)
  row += sum(lst)
  if row == 0:
    connect = False

if connect and tot == 6:
  print("Yes")
else:
  print("No")
