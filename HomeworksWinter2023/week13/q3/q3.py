t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    if (b-a) * (d-c) > a* c:
        print("YES")
    else:
        print("NO")
