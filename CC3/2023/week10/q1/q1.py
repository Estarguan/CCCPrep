import sys
input = sys.stdin.readline 

line1 = list(input().strip())
line2 = list(input().strip())

line1.sort(reverse=True)
line2.sort(reverse=True)
x = line2.count("*")
for i in range(len(line2)):
  if line2[i] != line1[i] and x != 0:
    line2.insert(i,line1[i])
    x -= 1
    line2.pop()
if line1 == line2:
  print("A")
else:
  print("N")