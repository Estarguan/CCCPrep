def f(n):
    if memo[n] != 0:
        return memo[n]
    if n <= 1:
        memo[n] = 1
        return memo[n]
    ans = 1
    for i in range(n-2,-1,-2):
        ans += f(i)
    memo[n] = ans
    return memo[n]

memo = [0]*65
n = int(input())
print(f(n))

#another method print(2**(int(input())//2))
