from itertools import permutations
num = input()
digits = list(num)
ans = 100000000000000000000000
for perm in permutations(digits):
    if int("".join(perm)) > int(num):
        if int("".join(perm)) < ans:
            ans = int("".join(perm))
print(ans if ans != 100000000000000000000000 else 0)
