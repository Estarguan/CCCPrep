import sys
input = sys.stdin.readline


def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True
n = int(input())

for i in range(n,2*10**20):
  if is_prime(i):
    print(i)
    break