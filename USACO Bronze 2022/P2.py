for i in range(int(input())):
    n,k = map(int,input().split())
    cows = input()
    count = 0
    G = 0
    H = 0
    if k == 0:
        print(cows)
        print(len(cows))
    else:
        for i in range(n):
            if cows[i] == "G":
                if G == 0:
                    G += k
                    count += 1
                if abs(i-G) > k:
                    G += k
                    count += 1
            elif cows[i] == "H":
                if H == 0:
                    H += k
                    count += 1
                if abs(i-H) > k:
                    H += k
                    count += 1
        print(count)
        print(cows)