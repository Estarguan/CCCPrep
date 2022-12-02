import sys
input = sys.stdin.readline

num = int(input())
a = []
for i in range(num):
    a.append(int(input()))
while True:
    op = int(input())
    if (op == 77): break
    if (op == 99):
        n = int(input()) - 1
        percent = int(input())
        left = a[n]*percent/100
        right = a[n] - left
        a[n] = left
        a.insert(n+1, right)
    if(op == 88):
        n = int(input()) - 1
        a[n] += a[n+1]
        a.pop(n+1)
for i in range(len(a)):
    print(round(a[i]), end= ' ')
