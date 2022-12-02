import sys
input = sys.stdin.readline

n1 = int(input().strip())
n2 = int(input().strip())
n3 = int(input().strip())
n4 = int(input().strip())

scam = True
if n1 != 8 and n1 != 9:
    scam = False
if n4 != 8 and n4 != 9:
    scam = False
if n2 != n3:
    scam = False

if scam:
    print("ignore")
else:
    print("answer")
