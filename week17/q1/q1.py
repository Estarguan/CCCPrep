import sys
input = sys.stdin.readline

max = int(input())
A,B,C = map(int,input().split())
if A+4*B+7*C <= max:
    print("Time to go shopping!")
else:
    print("You cannot afford them all.")
