def toBase10(b1,n,b2):
  base_10 = 0
  for i,digit in enumerate(reversed(str(n))):
    base_10 += int(digit)*(b1**i)
  
  digits = []
  while base_10>0:
      digits.append(str(base_10%b2))
      base_10 //= b2
  return ''.join(reversed(digits))



q = int(input())
for i in range(q):
  b1,n,b2 = map(int,input().split())
  ans = toBase10(b1,n,b2)
  print(ans)
