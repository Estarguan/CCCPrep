import sys
input = sys.stdin.readline

alpha = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

amount = 0
num = int(input())
line = list(input().strip())
starcnt = 0
for i in line:
    if i != "*":
        amount += ord(i)-96
    else:
        starcnt += 1
if starcnt == 0:
    if amount != num:
        print("Impossible")
    else:
        print("".join(line))
else:
    for i in range(len(line)):
        if amount >= num and starcnt > 0:
            print("Impossible")
            sys.exit()
        if line[i] == "*":
            needed =  (num-amount)-(starcnt-1)*26
            if needed <= 1:
                line[i] = "a"
                amount += 1
                starcnt -= 1
            else:
                if needed > 26:
                    print("Impossible")
                    sys.exit()
                else:
                    line[i] = alpha[needed]
                    amount += needed
                    starcnt -= 1
    print("".join(line))