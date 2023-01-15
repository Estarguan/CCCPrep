n = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = 0
tuition = 0

for i in range(n):
    fee = nums[i]
    money = (n - i) * fee
    if money > ans:
        ans = money
        tuition = fee

print(ans, tuition)