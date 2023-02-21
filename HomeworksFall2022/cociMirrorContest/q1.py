import sys
input = sys.stdin.readline

n, r, s = map(int, input().strip().split())
for x in range(n):
    mat = []
    max, min = -1, r+1
    for y in range(r):
        mat.append(input().strip())
    for i in range(s):
        for j in range(r):
            if mat[j][i] == "#":
                if j+1 > max:
                    max = j+1
                    print(max)
                if j+1 < min:
                    min = j+1
                    print(min)
    print(max-min)
