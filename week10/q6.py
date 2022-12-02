import sys
input = sys.stdin.readline

g = int(input())
for _ in range(g):
    num = int(input().strip())
    bin = []
    while num != 0:
        if num % 2 == 1:
            bin.insert(0,1)
            num = num//2
        else:
            bin.insert(0,0)
            num /= 2
    ans = 0
    for i in range(len(bin)):
        if bin[i] == 1:
            ans += 2**i
    print(ans)
