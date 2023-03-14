from itertools import combinations
h = int(input())
n = int(input())
min = 100000000000000000000
heights = []
for i in range(n):
    heights.append(int(input()))
for i in range(1,n+1):
    for x in combinations(heights,i):
        if sum(x) == h:
            if len(x) < min:
                min = len(x)
print(min if min != 100000000000000000000 else 0)