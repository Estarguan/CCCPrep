import sys
input = sys.stdin.readline

books = input().strip()

ans = 0
wrong_L = 0
wrong_M = 0
a = 0
b = 0
m = books.count("L")
n = books.count("M")
for i in books[:m]:
    if i != "L":
        wrong_L += 1
        if i == "M":
            a += 1
for i in books[m:m+n]:
    if i != "M":
        wrong_M += 1
        if i == "L":
            b += 1
ans = wrong_L + wrong_M - min(a, b)
print(ans)