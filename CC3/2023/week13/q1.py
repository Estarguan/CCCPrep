import sys
input = sys.stdin.readline 

idx = 1
n,q = map(int,input().split())
notes = []
for i in range(n):
  ai = int(input())
  for j in range(ai):
    notes.append(idx)
  idx += 1
  

for i in range(q):
  ti = int(input())
  print(notes[ti])
