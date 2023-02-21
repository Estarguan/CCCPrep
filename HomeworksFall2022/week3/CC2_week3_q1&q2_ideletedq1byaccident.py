import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    print(num, "X", i+1, "=", *(i+1))
