n = int(input())
nums = list(map(int,input().split()))

ans = 0
for i in range(n):
  ans = (ans+nums[i]) % int(1e9+7)
print((ans*(2**(n-1)))% int(1e9+7))