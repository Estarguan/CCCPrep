
def backtrack(n):
    global ans
    t1,t2 = games[n]
    
    scores[t1-1] += 3
    if n != 5-G:
        backtrack(n+1)
    if scores[T-1] == max(scores) and scores.count(max(scores)) == 1 and n == 5-G:
        ans += 1
    scores[t1-1] -= 3

    scores[t2-1] += 3
    if n != 5-G:
      backtrack(n+1)
    if scores[T-1] == max(scores) and scores.count(max(scores)) == 1 and n == 5-G:
        ans += 1
    scores[t2-1] -= 3

    scores[t1-1] += 1
    scores[t2-1] += 1
    if n != 5-G:
      backtrack(n+1)
    if scores[T-1] == max(scores) and scores.count(max(scores)) == 1 and n == 5-G:
        ans += 1
    scores[t1-1] -= 1
    scores[t2-1] -= 1
games = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
scores = [0,0,0,0]
ans = 0
T,G = int(input()),int(input())
for i in range(G):
    a,b,sa,sb = map(int,input().split())
    if sa == sb:
        scores[a-1] += 1
        scores[b-1] += 1
    elif sa > sb:
        scores[a-1]+= 3
    elif sa < sb:
        scores[b-1]+=3
    games.remove((a,b))

backtrack(0)
print(ans)