n = int(input())
tog, notog, groups, count = {},{},{},0

for i in range(n):
  tog[i] = input().split()
y = int(input())
for i in range(y):
  notog[i] = input().split()
g = int(input())
for i in range(g):
  group = input().split()
  for j in range(3):
    groups[group[j]] = i

for k,v in tog.items():
  if groups[v[0]] != groups[v[1]]:
    count += 1

for k,v in notog.items():
  if groups[v[0]] == groups[v[1]]:
    count += 1
print(count)
