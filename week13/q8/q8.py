R, C = map(int,input().split())
lst = [list(map(int,input().split())) for i in range(R)]
for i in range(int(input())):
    col = int(input())
    lst.sort(key = lambda x : x[col-1])
for i in lst:
    print(" ".join(map(str, i)))
