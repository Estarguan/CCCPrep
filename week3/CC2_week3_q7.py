import sys
input = sys.stdin.readline

letters = list(map(int, input().split(" ")))
letters.sort()
A = letters[0]
B = letters[1]
C = int(letters[-1]) - A - B

print(A, B, C)
