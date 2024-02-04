n = int(input())
ans = 0
for i in range(n):
  rem = n-4*i
  if rem == 0:
    ans += 1
  elif rem < 0:
    break
  else:
    if rem % 5 == 0:
      ans += 1
print(ans)
