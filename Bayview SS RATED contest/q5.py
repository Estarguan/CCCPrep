n = int(input())

trees = list(map(int, input().split()))
cnt = 1
def cutting(lst, cnt,index):
    temp2 = lst.copy()
    temp = lst.copy()
    for y in range(index, len(temp)):
        if temp[y] % 2 == 0:
            temp.insert(y+1, temp[y] // 2)
            temp[y] //= 2
            cnt += 1
            return cutting(temp,cnt, y)
    for z in range(index+1, len(temp)):
        if temp2[z] % 2 == 0:
            temp2.insert(z+1, temp2[z] // 2)
            temp2[z] //= 2
            cnt += 1
            return cutting(temp,cnt,z)
    return cnt
for x in range(len(trees)):
    if trees[x] % 2 == 0:
        cnt = cutting(trees,cnt,x)
print(cnt)

#i tried my best
