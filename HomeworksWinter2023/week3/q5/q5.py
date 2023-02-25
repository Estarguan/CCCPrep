n = int(input())
if n % 2 == 0:
    half = int(n/2)
else:
    half = int(n/2) + 1
tides = sorted(list(map(int, input().split())))
low = sorted(tides[0:half], reverse=True)
high = tides[half:]
for i in range(int(n/2)):
    print(low[i], high[i], end=" ")
if n % 2 == 1:
    print(low[-1])
