import sys
input = sys.stdin.readline

stringa,stringb=input().strip(),input().strip()
diff = abs(ord(stringb[0])-ord(stringa[0]))
print(diff)
for x,y in zip(stringa,stringb):
    print(abs(ord(y)-ord(x)))
    print(y,x)
    if abs(ord(y)-ord(x)) != diff:
        print("No")
        break
else:
    print("Yes")
