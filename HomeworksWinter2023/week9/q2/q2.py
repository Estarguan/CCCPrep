n,q = map(int,input().split())

shapes = ['' for i in range(n)] 
for i in range(q):
    a,b,c = input().split()
    if a == "set":
        shapes[int(c)-1] = b
    elif a == 'get':
        if shapes[int(c)-1] == b:
            print(1)
        else:
            print(0)