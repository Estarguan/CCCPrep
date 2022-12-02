import sys
input = sys.stdin.readline

h, m, count, N = 12, 0, 0, int(input())
for i in range(N%720):
    m += 1
    if m >= 60:
        h,m = h+1, 0
    if h > 12:
        h -= 12
    a,b,c,d = h//10, h%10, m//10, m%10
    if a == 0 and b-c == c-d:
        count += 1
    elif a != 0 and a-b == b-c and b-c == c-d:
        count += 1
print(N//720 * 31 + count)
