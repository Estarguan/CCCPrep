n,k,x = map(int,input().split())
for i in range(k-1):
  if (2**(n-1)-1 * (k-1) + i)%k == x:
    for j in range(n-1):
      print(k-1,end = "")
    print(i)