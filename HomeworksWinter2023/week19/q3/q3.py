n = int(input())
ans = 0
x,y = map(int,input().split())
R = int(input())
for i in range(R):
  l,r = map(int,input().split())
  if l < x and r < x:
    continue
  if l > y and r > y:
    continue
  if l < x:
    l = x
  if r > y:
    r = y

  ans += r-l+1                                        
print(ans)
  
