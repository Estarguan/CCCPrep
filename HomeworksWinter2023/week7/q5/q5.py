n,s = map(int,input().split())
dict={}
for i in range(int(n/s)):
    dict[i] = list()
    countries=map(int,input().split())
    for j in countries:
        dict[i].append([j])
print(dict)