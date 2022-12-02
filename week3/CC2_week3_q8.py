for i in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        low = lst.index(i)
        hi = lst.index(i+1)
        if low > hi:
            lst.pop(low)
            lst.insert(0, i)
            ans += low
    print(ans)
