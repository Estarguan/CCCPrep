import math

n, angle = map(int,input().split())
closest = 10000000000000000
ans = 0
for i in range(n):
  x,y = map(int,input().split())
  ang = math.degrees(math.atan2(y,x))
  if ang < 0:
    ang += 360
  if angle > 180 and ang < 180:
    if abs(360-angle+ang)<closest:
      closest = abs(360-angle+ang)
      ans = i+1
  if abs(ang-angle) < closest:
    closest = abs(ang-angle)
    ans = i+1
print(ans)