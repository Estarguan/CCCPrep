import sys
input = sys.stdin.readline

month =int(input().strip())
day = int(input().strip())

if month > 2:
    print("After")
elif month < 2:
    print("Before")
elif month == 2 and day > 18:
    print("After")
elif month == 2 and day < 18:
    print("Before")
else:
     print("Special")
