import sys
input = sys.stdin.readline

num = int(input())
x,y = [], []
for i in range(num):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
ans = 0
for i in range(num): #take i as the right angle
    for j in range(num): #check that i and j are parallel with the right axis
        for k in range(num): # check that i and k are parallel with y axis
            if y[i] == y[j] and x[i] == x[k]:
                ans = max(ans, abs(x[i]-x[j]) * abs(y[i] - y[k]))
print(ans)
