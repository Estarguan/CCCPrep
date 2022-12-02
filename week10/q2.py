import sys
input = sys.stdin.readline

letters = ("S", "H", "I", "N", "O", "Z", "X")
str = input().strip()
YES = True
for i in str:
    if i not in letters:
        YES = False
        break
print("YES" if YES else "NO")
