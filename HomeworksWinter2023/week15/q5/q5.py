for _ in range(10):

  R,T,A = input().split()
  
  A = list(A)
  ans = len(A)
  rules = {}
  lengths = {}
  letters = {}
  
  for j in A:
    letters[j]=letters.get(j,0)+1
  for i in range(int(R)):
    C, S = input().split()
    rules[C] = S
    lengths[C]= len(S)
    
  for i in range(int(T)):
    
    key = []
    for k in letters.keys():
      key.append(k)
    changed = {}
    for k in key:

      if k in rules:
        if k in changed:
          amount = letters[k] - changed[k]
          letters[k] = letters.get(k,0)-letters[k] + changed[k]
        else:
          amount = letters[k]
          letters[k] = letters.get(k,0)-letters[k]

        for z in rules[k]:
          letters[z] = letters.get(z,0) + amount
          changed[z] = amount
    print(letters)
    for j in range(len(A)):
      if A[j] in rules:
        A[j] = rules[A[j]]



    A = "".join(A)
    A = list(A)
    A = [A[0],A[-1]]

  
  print(A[0]+A[-1], ans)
  