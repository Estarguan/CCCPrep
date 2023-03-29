n,k = map(int,input().split())
nums = list(map(int, input().split()))
want = sorted(nums)
i = 0
changed = False
while nums != want:
  if nums[i] > nums[i+k]:
    nums[i],nums[i+k] = nums[i+k],nums[i]
    changed = True
  else:
    i += 1
  if i==n-1 or i + k > n-1:
    if changed:
      i = 0
      changed = False
    else:
      break
if want == nums:
  print('YES')
else:
  print('NO')
