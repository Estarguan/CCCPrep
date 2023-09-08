import sys
input = sys.stdin.readline 

num = int(input())
line = input().strip()

late = 0
waiting = 0
while line != "EOF":
  if line == "TAKE":
    waiting += 1
    late += 1
    num += 1
    if num > 999:
      num = 1
  elif line == "SERVE":
    waiting -= 1
  elif line == "CLOSE":
    print(str(late) + " " + str(waiting) + " " + str(num))
    late = 0
    waiting = 0
  line = input().strip()
  