n= int(input())
nums = list(map(int,input().split()))
nums.sort()
if n % 2 == 1:
    print(int(nums[int(n//2)]))
else:
    print(int((nums[int(n/2)]+nums[int(n/2-1)])/2))
