for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    updown = True
    for i in range(1 , n, 2):
        if a[i] == 0:
            a[i] = int(1e9 + 1)
    for i in range(1, n, 2):
        if a[i-1] >= a[i] or (i+1 < n and a[i] <= a[i+1]):
            updown = False
    downup = True
    for i in range(0, n, 2):
        if b[i] == 0:
            b[i] = int(1e9 + 1)
    for i in range(0, n, 2):
        if (i-1 >= 0 and b[i-1] >= b[i]) or (i+1 < n and b[i] <= b[i+1]):
            downup = False
    print("YES") if updown or downup else print("NO")
