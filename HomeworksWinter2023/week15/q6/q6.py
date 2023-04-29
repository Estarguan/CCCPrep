from itertools import combinations
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    stop = False
    n = int(input())
    for i in range(2,n*2):
        b = 2*n-i
        if is_prime(i) and is_prime(b):
            print(i,b)
            break             
