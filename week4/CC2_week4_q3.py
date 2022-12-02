import sys
input = sys.stdin.readline

A = 0
A += int(input().strip())*3
A += int(input().strip())*2
A += int(input().strip())
B = 0
B += int(input().strip())*3
B += int(input().strip())*2
B += int(input().strip())

if B==A:
    print("T")
elif B > A:
    print("B")
else:
    print("A")
