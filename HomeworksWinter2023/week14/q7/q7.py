import sys
input = sys.stdin.readline


def f(n):
  if n == 0:
    return "Good writing is good writing is good writing." 
  else:
    
      
      return "Good writing is good " + f(n-1) + " writing is good " + f(n-1) + " is good writing."
q = int(input())
for i in range(q):
  n,k = map(int,input().strip().split())
  line = f(n)

  try:
    print(line[k-1]) 
  except:
    print('.')