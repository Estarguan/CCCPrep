count = 0
for i in range(int(input())):
    m,o = map(int,input().split())
    if m > o:
        count += 1
print(count)