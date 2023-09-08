s = input()
ans = 0
for i in range(len(s)):
  try:
    if s[i] == '2' and s[i+1] != '5':
      ans += 1
  except:
    if s[i] == '2':
      ans += 1
print(ans)