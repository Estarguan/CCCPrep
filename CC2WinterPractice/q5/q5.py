import sys
input = sys.stdin.readline

stringa,stringb=input().strip(),input().strip()
diff = abs(ord(stringb[0])-ord(stringa[0]))
print(diff)
