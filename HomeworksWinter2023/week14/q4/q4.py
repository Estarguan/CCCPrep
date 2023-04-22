import sys 
input = sys.stdin.readline
import math

q = int(input())
for _ in range(q):
    
    t = int(input())
    undef = t
    one_loss = 0
    eliminated = 0
    i = 0
    while True:
      print("Round " + str(i) + ": " + str(undef) + " undefeated, " + str(one_loss) + " one-loss, " + str(eliminated) + " eliminated")
      
      if one_loss == 1 and undef == 1:


        one_loss += 1
        undef -= 1
        i += 1
        print("Round " + str(i) + ": " + str(undef) + " undefeated, " + str(one_loss) + " one-loss, " + str(eliminated) + " eliminated")
        one_loss -= 1
        eliminated += 1
        print("Round " + str(i+1) + ": " + str(undef) + " undefeated, " + str(one_loss) + " one-loss, " + str(eliminated) + " eliminated")
        print("There are " + str(i+1) + " rounds.")
        if _ != q-1:
          print()
        break
      elif undef == 1:
         eliminated += math.floor(one_loss / 2)
         one_loss = math.ceil(one_loss/2)
         i += 1
      elif one_loss == 1:
        one_loss += math.floor(undef / 2)
        undef = math.ceil(undef/2)
        i += 1
      else:
        i += 1
        eliminated += math.floor(one_loss / 2)
        one_loss -= math.floor(one_loss / 2)
        one_loss += math.floor(undef / 2)
        undef = math.ceil(undef/2)

      