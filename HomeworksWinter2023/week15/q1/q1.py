n = int(input())
nums = list(map(int,input().split()))

odd = []
even = []
for i in range(n):
  if nums[i] % 2 == 0:
    even.append(nums[i])
  else:
    odd.append(nums[i])

print(len(odd)//2+len(even)//2)