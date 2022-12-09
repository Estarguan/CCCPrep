import sys
input = sys.stdin.readline

n = int(input())
a = list(input().strip())
b= list(input().strip())
tochange = []
for i in range(n):
    if a[i] != b[i]:
        tochange.append(i)
together = 0
for i in range(len(tochange)-1):
    if tochange[i+1]-tochange[i]==1:
        together += 1
print(len(tochange)-together)
