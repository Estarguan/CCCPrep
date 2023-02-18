p, c = int(input()),int(input())
score = 50*p -10*c
if p > c:
  score += 50
print(score)