def sol1():
    n = int(input())
    comps = []
    for i in range(n):
        comp = input().split()
        comps.append([str(comp[0]), 2*int(comp[1])+3*int(comp[2])+int(comp[3])])
    comps.sort(key = lambda x : x[1])

    a = []
    # find all MAX
    for v in comps:
        if v[1] == comps[len(comps)-1][1]:
            a.append(v)

    b = []
    # find all second MAX
    for v in comps:
        if v[1] == comps[len(comps)-2][1]:
            b.append(v)
    a.sort()
    b.sort()

    if a:
        print(a[0][0])
        maxName = a[0][0]
        for i in b:
            if i[0] != maxName:
                print(i[0])
                break
    else:
        print("")

def sol2():
    n = int(input())
    comps = []
    for i in range(n):
        comp = input().split()
        comps.append([str(comp[0]), 2 * int(comp[1]) + 3 * int(comp[2]) + int(comp[3])])
    comps.sort(key=lambda x: x[1])
    maxName, maxVal = "", 0
    for i in comps:
        if i[1] > maxVal:
            maxName = i[0]
            maxVal = i[1]
        elif i[1] == maxVal:
            if i[0] < maxName:
                maxName = i[0]
                maxVal = i[1]

    print(maxName)
    maxName2,maxVal2 = "", 0
    for i in comps:
        view = i
        if maxVal2 < i[1] <= maxVal:
            if i[0] != maxName:
                maxName2 = i[0]
                maxVal2 = i[1]
        elif i[1] == maxVal2:
            if i[0] != maxName:
                if i[0] < maxName2:
                    maxName2 = i[0]
    print(maxName2)


def sol3():
    n = int(input())
    pc = []

    for _ in range(n):
        pc.append(input().split())

    pc = sorted(pc, key=lambda x: x[0])

    pc = sorted(pc, key=lambda x : (2 * (int(x[1])) + 3 * (int(x[2])) + (int(x[3]))), reverse= True)

    if len(pc) == 0:
        print(" ")
    else:
        if len(pc) == 1:
            print(pc[0][0])
        else:
            print(pc[0][0])
            print(pc[1][0])
sol3()