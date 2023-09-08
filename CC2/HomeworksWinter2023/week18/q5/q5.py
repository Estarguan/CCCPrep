n,k,x = map(int,input().split())

for j in range(n-1):
  print(k-1,end = " ")

print((x-(2**(n-1)+1)%k))


