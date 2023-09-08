n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
n1, n2, count = 0,0,0
for i in range(n):
    n1 += l1[i]
    n2 += l2[i]
    if n1 == n2:
        count = i+1
print(count)