n = int(input())
heights = list(map(int, input().strip().split()))
widths = list(map(int,input().strip().split()))

ans = 0
for i in range(n):
  ans += widths[i]*(heights[i] + heights[i+1])/2
print(ans)