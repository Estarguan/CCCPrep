n,t = map(int, input().split())
execs = list(map(int, input().split()))
cnt = 0
choice1 = []
temp = -1
for i in range(n):
    if cnt + execs[i] <= t:
        temp += 1
        cnt += execs[i]
        choice1.append(execs[i])
    else:
        break

try:
    if max(choice1) > execs[temp+1]:
        execs.pop(execs.index(max(choice1)))
    else:
        execs.pop(temp+1)
except ValueError:
    execs.pop(temp+1)
except IndexError:
    pass
cnt = 0
choice1 = []
for i in range(n-1):
    if cnt + execs[i] <= t:
        cnt += execs[i]
        choice1.append(execs[i])
    else:
        break
print(len(choice1))
