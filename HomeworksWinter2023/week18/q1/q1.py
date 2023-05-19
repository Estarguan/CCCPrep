s = list(input().strip())
t = list(input().strip())
S = len(s)
if len(t) > len(s):

  for i in range(len(s)):
    if s[i] != t[i]:
      a = i
      break
    else:
      a = len(s)
else:
  for i in range(len(t)):
    if s[i] != t[i]:
      a = i
      break
  else:
    a = len(t)
s = s[:a]

print(S-a+len(t)-a)

