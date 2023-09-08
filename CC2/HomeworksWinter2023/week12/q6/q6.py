import sys
from collections import deque
input = sys.stdin.readline 

n = int(input())
schedule = list(map(int,input().strip().split()))
if len(set(schedule)) == 1:
   print(-1)
   sys.exit()
notProtected = [True]*(n+1)
rob = []
for i in range(n):
    if i != n-1:
      #schedule[i+1] in notProtected
      if notProtected[schedule[i+1]] and schedule[i] != schedule[i+1]:
        rob.append(schedule[i+1])
        notProtected[schedule[i+1]] = False
      else:
          rob.append(0)
    else:
        if notProtected[schedule[0]]:
          rob.append(schedule[0])
          notProtected[schedule[0]] = False
        else:
           rob.append(0)

q = deque()
for i in range(1,n+1):
   if notProtected[i]:
      q.append(i)
for i in range(n):
   if rob[i] == 0:
      rob[i] = q.popleft()
for i in rob:
   print(i, end = ' ')