import sys
input = sys.stdin.readline

Ant = 100
Dav = 100

for i in range(int(input().strip())):
    Antr, Davr = map(int, input().split())
    if Davr > Antr:
        Ant -= Davr
    elif Antr > Davr:
        Dav -= Antr
print(Ant)
print(Dav)
