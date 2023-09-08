import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,a = int(input()), list(map(int,input().split()))
    psa,vis = 0,set()
    for x in a:
        psa += x
        vis.add(psa)
    if psa == 0:
        print(0)
    else:
        for x in range(1,psa+1):
            if psa%x != 0:continue
            work = True
            for i in range(x,psa+1,x):
                if i not in vis:
                    work = False
                    break
            if work:
                print(n-psa//x)
                break
