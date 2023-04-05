changes = {
  'A':2,
  'B':2,
  'C':2,
  'D':3,
  'E':3,
  'F':3,
  'G':4,
  'H':4,
  'I':4,
  'J':5,
  'K':5,
  'L':5,
  'M':6,
  'N':6,
  'O':6,
  'P':7,
  'Q':7,
  'R':7,
  'S':7,
  'T':8,
  'U':8,
  'V':8,
  'W':9,
  'X':9,
  'Y':9,
  'Z':9,
}

n = int(input())
for i in range(n):
  count = 0
  count2 = 0
  count3 = 0
  line = list(input())
  for i in range(len(line)):
    if line[i] == '-':
      continue
    count += 1
    if line[i] in changes:
      print(changes[line[i]], end='')
      count3 += 1
    else:
      print(line[i],end='')
      count3 += 1
    if count2 < 2 and count == 3:
      print('-', end='')
      count2 += 1
      count = 0    
    if count3 >= 10:
      break
  print()
  