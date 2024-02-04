import sys
input = sys.stdin.readline 

n = int(input())
str = input().strip()
if str[0] != str[-1]:
  print(n)
else:
  cnt = 1
  for i in range(n-1):
    cnt += str [i] == str[i+1]
  print(n-cnt if cnt<n else 1)