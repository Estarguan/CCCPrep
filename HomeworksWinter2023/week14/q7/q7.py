import sys
input = sys.stdin.readline

memo = ["" for i in range(31)]
memo[0] = "Good writing is good writing is good writing." 
def f(n):
  if n == 0:
    return "Good writing is good writing is good writing." 
  else:
    
      
      return "Good writing is good " + f(n-1) + " writing is good " + f(n-1) + " is good writing."
q = int(input())
for i in range(q):
  n,k = map(int,input().strip().split())
  f(n)
  line = memo[n]

  try:
    print(line[k-1]) 
  except:
    print('.')