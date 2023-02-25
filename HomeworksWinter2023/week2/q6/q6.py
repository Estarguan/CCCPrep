N,M = map(int, input().split())
on = 0
lights = [0 for i in range(N+1)]
for i in range(M):
  l,r = map(int, input().split())
  l,r = l-1,r-1
  lights[l] += 1
  lights[r+1] -= 1
psa =[lights[0]]
for i in range(1,len(lights)):
  psa.append(lights[i] + psa[i-1])
for i in psa:
  if i % 2 == 1:
    on += 1
print(on)
