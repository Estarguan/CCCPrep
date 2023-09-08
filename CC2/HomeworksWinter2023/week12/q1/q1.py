import sys
input = sys.stdin.readline 

quer = list(map(int,input().strip().split()))
n = quer.count(0)
if n == 0:
    print("NO")
elif n == 3:
    print("YES")
elif n == 2:
    for i in range(3):
        if quer[i] == 0:
            continue #3 1 0
        else:
            if quer[i]-1 == i:
                print("NO")
                sys.exit()
            else:
                print("YES")
                sys.exit()
else:
   for i in range(3):
    if quer[i]-1 == i:
      print("NO")
      sys.exit()
    if quer[i] == 0:
        if i == 2:
           print("YES")
           sys.exit()
        else:
          continue
    else:
        
        if quer[quer[i]-1] == 0:
          if i == 2:
           print("YES")
           sys.exit()
          else:
            continue
        else:
            if quer[quer[i]-1] != i+1 and quer[quer[i]-1] != quer[i]:
              print("YES")
              sys.exit()
            else:
               print("NO")
               sys.exit()
          