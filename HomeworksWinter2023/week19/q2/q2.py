n = int(input())
nums = list(map(int,input().split()))
ans = 0
temp = 0
for i in range(len(nums)):
  if nums[i] % 2 == 0:
    temp += nums[i]
  else:
    if temp > ans:
      ans = temp
    temp = 0
if temp > ans:
  ans = temp
print(ans)