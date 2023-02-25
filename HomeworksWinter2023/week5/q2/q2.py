import sys
input = sys.stdin.readline

n = int(input())
actions = list(input())

enemyBullets = 0
score = 0
bullets = 0
for i in actions:
    if i == "B":
        bullets += 1
    elif i == "R":
        enemyBullets += 1
        if bullets > 0:
          bullets -= 1
          score += 1
        else:
            bullets += 1
    elif i == "F":
        if enemyBullets == 0:
            if bullets > 0:
                score += 1
                bullets -= 1
            else:
                bullets += 1
        else:
          enemyBullets -= 1
print(score)