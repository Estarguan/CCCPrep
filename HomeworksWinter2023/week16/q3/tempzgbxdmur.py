a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

bools = [False,False,False]
ans = 0
for i in range(3):
  if b[i] == a[i-1]:
    ans += c[i]
    bools[i] = True

if bools[0] and bools[2] and not bools[1]:
  print(0)


print(ans)