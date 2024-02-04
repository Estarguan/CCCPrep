import sys
input = sys.stdin.readline 

n = int(input())
alphabet = [0,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


lst = []

while n > 0:
  remainder = n % 26
  if remainder == 0:
      remainder = 26  # special case for multiples of 26
      n -= 1  # decrement n to handle carryover
  lst.append(remainder)

  n//=26
for i in range(len(lst)-1,-1,-1):
  print(alphabet[lst[i]],end="")