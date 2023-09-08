n,a,b = map(int,input().split())
tom,an = 0,0
for i in range(n):
    h1,h2 = map(int,input().split())
    if h1 < a:
        an += 1
    else:
        an += 2
    if h2 < b:
        tom += 1
    else:
        tom += 2
if tom==an:
    print("Tie!")
elif tom<an:
    print("Tommy wins!")
else:
    print("Andrew wins!")