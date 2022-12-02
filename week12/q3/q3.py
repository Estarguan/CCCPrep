t1,t2 = int(input()), int(input())
diff = t1-t2
num = 2
while diff >= 0:
    temp = diff
    diff = t2-diff
    t2 = temp
    num += 1
print(num)
