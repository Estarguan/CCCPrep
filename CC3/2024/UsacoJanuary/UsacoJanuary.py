import sys
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
  n = int (input ())
  cows = list(map(int,input().split()))
  answer = set()
  #hays = set(cows)
  #for i in hays:
  for i in range(len(cows)):
    try:
      if cows[i] == cows[i+1]:
        answer.add(cows[i])
        
      if cows[i] == cows[i+2]:
        answer.add(cows[i])
        
    except:
      continue

  
  if len(answer) > 0:
    lst = list(answer)
    lst.sort()
    print(*lst)
  else:
    print(-1)