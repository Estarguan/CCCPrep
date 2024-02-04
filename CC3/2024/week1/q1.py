import sys
input = sys.stdin.readline 

n = int(input())
s = input().strip()
rgb = [[0,0]]

for i in range(len(s)):
  if s[i] == "R":
    rgb[-1][0] += 1
  elif s[i] == "B":
    rgb[-1][1] += 1
  elif s[i] == "G":
    rgb.append([0,0])

ans = 0
for i in range(len(rgb)-1):
  ans += rgb[i][0] * rgb[i+1][1]
print(ans)