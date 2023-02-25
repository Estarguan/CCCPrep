import sys
input = sys.stdin.readline
time = 0
people = {}
sent = {}
recieved = {}
n = int(input())
for i in range(n):
    a,b = input().strip().split()
    if b not in people and a != "W":
        people[b] = 0
    if a == "R":
        recieved[b] = [time,False]
        time += 1
    elif a == "W":
        time -= 1
        time += int(b)
    elif a == "S":
        if b in recieved:
            people[b] += time - recieved[b][0]
            recieved[b][1] = True 
        time += 1
for i in sorted(people.keys()):
    if not recieved[i][1]:
        print(i, -1)
    else:
        print(i, people[i])
