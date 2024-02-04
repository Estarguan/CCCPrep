import sys
input = sys.stdin.readline 

minSize = 1_000_000_000_000
n = int(input())
villages = []
for i in range(n):
  villages.append(int(input()))
villages.sort()
for i in range(1,n-1):
  x = (villages[i] - villages[i-1])/2 + (villages[i+1]-villages[i])/2
  if x < minSize:
    minSize = x
print(minSize)
