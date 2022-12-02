import sys
input = sys.stdin.readline

num = int(input().strip())
str = input().strip()

countA = 0
countB = 0

for i in range(num):
    if str[i] == "A":
        countA += 1
    elif str[i] == "B":
        countB += 1
if countA > countB:
    print("A")
elif countB > countA:
    print("B")
else:
    print("Tie")
