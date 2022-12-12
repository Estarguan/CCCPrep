import sys
input = sys.stdin.readline

lst = ["_","_","M","M"]
n = int(input())


finans=""

for i in range(n//4):
    finans += "".join(lst)
for i in range(n%4):
    finans+= lst[i]
print(finans.count("M"))
print(finans)
