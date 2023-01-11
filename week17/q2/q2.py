import sys
input = sys.stdin.readline

n = int(input())
trees = list(map(int,input().strip().split()))
maxlen = 0
length = 1
for i in range(len(trees)-1):
    if trees[i] < trees[i+1]:
        length += 1
    else:
        if length > maxlen: maxlen = length
        length = 1
if length > maxlen: maxlen = length
print(maxlen)
maxlen = 0
length = 1
for i in range(len(trees)-1):
    if trees[i] > trees[i+1]:
        length += 1
    else:
        if length > maxlen: maxlen = length
        length = 1
if length > maxlen: maxlen = length
print(maxlen)
