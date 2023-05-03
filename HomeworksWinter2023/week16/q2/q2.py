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
if is_prime(n):
  print("prime")
else:
  print("not")