a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

bools = [False,False,False]
ans = 0
for i in range(3):
  if b[i] == a[i-1]:
    if c[i] > 0:
      ans += c[i]
    bools[i] = True

if bools[0] and bools[2] and not bools[1]:
  print(max(c[0],c[2]))

#elif bools[0] and bools[1] and bools[2]:
 # print(max(c[0]+c[1], c[1]+c[2]))
else:
  print(ans)