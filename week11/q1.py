import sys
input = sys.stdin.readline

lim, speed = int(input()), int(input())
if speed > lim:
    if speed-lim <= 20: f = 100
    elif 20 < speed-lim < 30: f = 270
    else: f = 500
    print("You are speeding and your fine is $" + str(f) + ".")
else:
    print("Congratulations, you are within the speed limit!")
