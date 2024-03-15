import sys
input = sys.stdin.readline

s, n = map(int,input().split())

rack = list(map(int,input().split()))
pile = list(map(int,input().split()))

for card in pile:
  added = False
  for i in range(len(rack)):
    try:
      if card == rack[i] - 1:
        rack[i-1] = card
        added = True
        break
    except:
      continue
  if added:
    continue
  for i in range(len(rack)):
    try:
      if card == rack[i] + 1:
        rack[i+1] = card
        added = True
        break
    except:
      continue

  if added:
    continue
  for i in range(len(rack)):
    try:
      if not rack[i] < rack[i+1] < rack[i+2] and rack[i] < card < rack[i+2]:
        rack[i+1] = card
        added = True
        break
    except:
      continue

  if added:
    continue
  for i in range(len(rack)):
    try:
      if rack[0] > rack[1] and card < rack[1]:
        rack[0] = card
        added = True
        break
    except:
      continue
  if added:
    continue
  for i in range(len(rack)):
    try:
      if card > rack[-2] and rack[-1] < rack[-2]:
        rack[-1] = card
        
        break
    except:
      continue
ans = 0
consectuive = 1

if rack == sorted(rack):
  ans += sum(rack)
  for i in range(len(rack)-1):
    if rack[i] == rack[i+1]-1:
      consectuive += 1
    else:
      if consectuive >= 3:
        ans += consectuive*5
      consectuive = 1
  if consectuive >= 3:
    ans += consectuive*5
else:
  for i in range(len(rack)):
    if rack[i] < rack[i+1]:
      ans -=1


print(ans)