import sys
input = sys.stdin.readline

n = int(input())
trees = []
prev = 0
for i in range(0,n):
  trees.append(int(input())+prev)
  prev = trees[i]
q = int(input())
for i in range(q):
  n1,n2 = map(int, input().split())
  print(trees[n2]-trees[n1-1] if n1 != 0 else trees[n2])
