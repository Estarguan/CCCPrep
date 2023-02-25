mom = input()
dad = input()
count = 0
mom_up, dad_up = 0, 0
genes = {
  "A":[False,False],
  "B":[False,False],
  "C":[False,False],
  "D":[False,False],
  "E":[False,False],
}
for i in range(10):
  count += 1
  if mom[i].isupper():
    mom_up += 1
  if dad[i].isupper():
    dad_up += 1
  if count == 2:
    if mom_up == 0 and dad_up == 0:
      genes[mom[i].upper()][1] = True
    if mom_up == 2 or dad_up == 2:
      genes[mom[i].upper()][0] = True
    count,mom_up,dad_up = 0,0,0
for _ in range(int(input())):
  isbaby = True
  baby = input()
  for i in baby:
    if i.islower():
      if genes[i.upper()][0] == True:
        isbaby = False
    elif i.isupper():
      if genes[i][1] == True:
        isbaby = False
  if isbaby:
    print("Possible baby.")
  else:
    print("Not their baby!")