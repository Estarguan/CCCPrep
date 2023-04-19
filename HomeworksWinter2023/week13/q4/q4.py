import sys
input = sys.stdin.readline 

n = int(input())
dir = input().strip()

if n%2 == 1:
    print(dir)
else:
    print("left" if dir == "right" else "right")