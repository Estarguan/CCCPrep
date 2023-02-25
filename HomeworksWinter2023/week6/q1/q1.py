attenders = {}
n = int(input())
days = []
for i in range(n):
  days.append(list(input()))
for i in range(5):
  count = 0
  for j in range(n):
    if days[j][i] == "Y":
      count += 1
  attenders[i+1] = count

largest = max(attenders.values())
ans = []
for i in range(5):
  if attenders[i+1] == largest:
    ans.append(i+1)
if len(ans) == 1:
  print(ans[0])
else:
  for i in range(len(ans)):
    if i != len(ans)-1:
      print(ans[i], end =',')
    else:
      print(ans[i])
