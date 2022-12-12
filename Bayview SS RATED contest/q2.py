n = int(input())

for i in range(n):
    sev, ele = False, False
    num1,num2, = input().split()
    if len(num1) == 1:
        if num1 == "7":
            sev = True
    else:
        if num1[-1] == "7" and num1[-2] != "1":
            sev = True
        elif num1[-1] == "1" and num1[-2] == "1":
            ele = True
    if len(num2) == 1:
        if num2 == "7":
            sev = True
    else:
        if num2[-1] == "7" and num2[-2] != "1":
            sev = True
        elif num2[-1] == "1" and num2[-2] == "1":
            ele = True


    if sev and ele:
        print("YES")
    else:
        print("NO")
