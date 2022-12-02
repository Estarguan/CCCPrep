import sys
input = sys.stdin.readline

Str = input().strip()
if Str.count(":-)") == 0 and Str.count(":-(") == 0:
    print("none")
elif Str.count(":-)") > Str.count(":-("):
    print("happy")
elif Str.count(":-)") < Str.count(":-("):
    print("sad")
else:
    print("unsure")
