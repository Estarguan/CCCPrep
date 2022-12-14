n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
nums.sort(key = lambda x : str(x)[-1])

print(" ".join(map(str,nums)))