n = int(input())
lin1=input()
lin2=input()
count = 0
for i in range(n):
  if lin1[i] == "S" and lin2[i] == "S":
    count += 1
print("NO" if count > 2 else "YES")