import sys
input = sys.stdin.readline

dict = {}
for i in range(int(input())):
    name, num = input().strip().split()
    dict[int(num)] = [0, name]
for i in range(int(input().strip())):
    dict[int(input().strip())][0] += 1

mx, phone = 0, 0
for k, v in dict.items():
    if v[0] > mx or v[0] == mx and k<phone:
        mx, phone = v[0], k
print(dict[phone][1])
