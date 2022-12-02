import sys
input = sys.stdin.readline
sys.maxsize

n = int(input().strip())


high_x, high_y, low_x, low_y = -sys.maxsize-1, -sys.maxsize-1, sys.maxsize, sys.maxsize
for i in range(n):
    x,y = input().split(",")
    x,y = int(x), int(y)
    if x > high_x:
        high_x = x
    if x < low_x:
        low_x = x
    if y > high_y:
        high_y = y
    if y < low_y:
        low_y = y
print(str(low_x -1) + "," + str(low_y -1))
print(str(high_x+1) + "," + str(high_y+1))
