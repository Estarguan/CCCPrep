t = int(input())
for i in range(t):
  n,k = map(int,input().split())
  cows = list(input())
  result = ['.' for i in range(n)]
  stk = []
  lastg,lasth,ans = -n, -n,0
  for i in range(k):
    stk.append(i)
  for i in range(n):
    if (i+k<n):
      stk.append(i+k)
    if cows[i] == 'G':
      if abs(i-lastg) > k:
        lastg = stk.pop()
        ans += 1
        result[lastg] = 'G'
    else:
      if abs(i-lasth) > k:
        lasth = stk.pop()
        ans += 1
        result[lasth] = 'H'

  print(ans)
  print(''.join(result))
