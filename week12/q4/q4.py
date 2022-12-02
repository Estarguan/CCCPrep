com, num = input().split()
num = int(num)
dang = {
    0:{-1,-2,-3,-7},
    1:{-3,-7},
    2:{-3,-7},
    3:{-3,-4,-5,-7},
    4:{-5,-7},
    5:{-3,-4,-5,-7},
    6:{-3,-7},
    7:{-3,-4,-5,-6,-7},
    -1:{-5,-6,-7}
}
x,y = -1,-5
while(com != 'q'):
    safe = True
    if com == "l":
        for i in range(num):
            x-=1
            if x in dang.keys():
                if y in dang[x]:
                    safe = False
                else:
                    dang[x].add(y)
            else:
                dang[x] = {y}
        print(x, y, end =" ")
        print("safe" if safe else "DANGER")
        if not safe:
            break
    elif com == "r":
        for i in range(num):
            x+=1
            if x in dang.keys():
                if y in dang[x]:
                    safe = False
                else:
                    dang[x].add(y)
            else:
                dang[x] = {y}
        print(x, y, end=" ")
        print("safe" if safe else "DANGER")
        if not safe:
            break
    elif com == "d":
        for i in range(num):
            y-=1
            if x in dang.keys():
                if y in dang[x]:
                    safe = False
                else:
                    dang[x].add(y)
            else:
                dang[x] = {y}
        print(x, y, end=" ")
        print("safe" if safe else "DANGER")
        if not safe:
            break
    elif com == "u":
        for i in range(num):
            y+=1
            if x in dang.keys():
                if y in dang[x]:
                    safe = False
                else:
                    dang[x].add(y)
            else:
                dang[x] = {y}
        print(x, y, end=" ")
        print("safe" if safe else "DANGER")
        if not safe:
            break
    com, num = input().split()
    num = int(num)
