import sys
input = sys.stdin.readline

nums = []
for i in input().strip().split(" "):
    try:
        nums.append(float(i))
    except:
        if i == "+":
            temp = nums[-2] + nums[-1]
            nums.pop()
            nums.pop()
            nums.append(temp)
        elif i == "-":
            temp = nums[-2] - nums[-1]
            nums.pop()
            nums.pop()
            nums.append(temp)
        elif i == "*":
            temp = nums[-2] * nums[-1]
            nums.pop()
            nums.pop()
            nums.append(temp)
        elif i == "%":
            temp = nums[-2] % nums[-1]
            nums.pop()
            nums.pop()
            nums.append(temp)
        elif i == "^":
            temp = nums[-2] ** nums[-1]
            nums.pop()
            nums.pop()
            nums.append(temp)
        else:
            temp = nums[-2] / nums[-1]
            nums.pop()
            nums.pop()
            nums.append(temp)
print(nums[0])
