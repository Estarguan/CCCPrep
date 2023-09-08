n = int(input())
dic = {}
for i in range(n):
  a,b = input().split()
  dic[b] = a


bina = list(input())
s = ''
n
for i in range(len(bina)):
  s += bina[i]
  if s in dic:
    print(dic[s],end='')
    s = ''
  
print()