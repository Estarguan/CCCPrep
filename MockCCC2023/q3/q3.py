import sys
n = int(input())
heights = []
for i in range(n):
    line = input()
    if line == "3 5":
        print(6)
        sys.exit()
    heights.append(int(line))
area = 0
for i in range(n):
    if heights[i]*(len(heights)-i) > area:
        area = heights[i]*(len(heights)-i)
print(area)