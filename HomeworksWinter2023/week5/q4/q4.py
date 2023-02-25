import sys
input = sys.stdin.readline
vowels = ['a','e','i','o','u']

answers = []
n = int(input())
line = ['','','','']
for _ in range(n):
    for i in range(4):
        text = input().strip().lower().split()
        for j in range(len(text[-1])-1,-1,-1):
            view = text[-1][j]
            if text[-1][j] in vowels:
                line[i] = ''.join(text[-1][j:])
                break
        else:
            line[i] = text[-1]
    if line[0] == line[1] == line[2] == line[3]:
        answers.append("perfect")
    elif line[0] == line[1] and line[2] == line[3]:
        answers.append("even")
    elif line[0] == line[2] and line[1] == line[3]:
        answers.append("cross")
    elif line[0] == line[3] and line[1] == line[2]:
        answers.append("shell")
    else:
        answers.append("free")
for i in answers:
    print(i)