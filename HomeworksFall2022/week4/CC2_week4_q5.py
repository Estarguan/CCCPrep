import sys
input = sys.stdin.readline

for t in range(int(input())):
    s = input().strip()
    i, j, count = 0, 0, 0
    while i < len(s):
        while j < len(s) and s[j] == s[i]:
            j += 1
            count += 1
        print(count, s[i], end= ' ')
        i = j
        count = 0
    print()
