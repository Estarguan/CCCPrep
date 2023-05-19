import sys
import math

input = sys.stdin.readline

def prime(num):
    y = int(math.sqrt(num))
    for i in range(2,y+1):

        while num % i == 0:
            factors[i] = factors.get(i,0) + 1
            num /= i
            num = int(num)
    if num != 1:
        factors[num] = factors.get(num,0) + 1
    
            
for _ in range(5):
    factors = {}
    num = int(input())
    for i in range(2,num+1):
        prime(i)
    ans = ""
    for k, v in factors.items():
        ans += str(k) + "^" + str(v) + " * "
    print(ans[: -3])
