import sys
input = sys.stdin.readline

num1, num2, num3 = int(input().strip()), int(input().strip()), int(input().strip())

if num1 + num2 + num3 == 180:
    if num1 == num2 == num3:
        print("Equilateral")
    elif num1 == num2 or num1 == num3:
        print("Isosceles")
    elif num2 == num3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
