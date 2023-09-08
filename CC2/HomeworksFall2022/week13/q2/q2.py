n = int(input())
ans = []
cor = []
cnt = 0
for i in range(n):
    ans.append(input())
for i in range(n):
    cor.append(input())
for i in range(n):
    if ans[i] == cor[i]:
        cnt += 1
print(cnt)
