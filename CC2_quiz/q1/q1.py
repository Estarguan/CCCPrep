import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    if int(input()) % 3 ==0 :
        print("yes")
    else:
        print("no")
