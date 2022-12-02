import sys
sys.stdin.readline

S = int(input().strip())
M = int(input().strip())
L = int(input().strip())

happiness = S+2*M+3*L
if happiness >= 10:
    print("happy")
else:
    print("sad")
