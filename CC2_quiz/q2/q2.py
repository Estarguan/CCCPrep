import sys
input = sys.stdin.readline
stringa = input().strip()
stringb = input().strip()
maxcnt = 0
if len(stringb) >= len(stringa):
    cnt = 0
    for i in range(len(stringb)):
        for j in range(i+1, len(stringb)+1):
            view = stringb[i:j]
            print("i made it")
            if stringa.startswith(stringb[i:j]):
                cnt = j-i
                if cnt > maxcnt: maxcnt = cnt
            elif stringa.endswith(stringb[i:j]):
                cnt = j - i
                if cnt > maxcnt: maxcnt = cnt
        print()
else:
    cnt = 0
    for i in range(len(stringa)):
        for j in range(i + 1, len(stringa) + 1):
            view = stringa[i:j]
            if stringb.startswith(stringa[i:j]):
                cnt = j - i
                if cnt > maxcnt: maxcnt = cnt
            elif stringb.endswith(stringa[i:j]):
                cnt = j - i
                if cnt > maxcnt: maxcnt = cnt
print(maxcnt)
