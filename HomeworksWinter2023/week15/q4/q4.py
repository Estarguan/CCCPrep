import sys
input = sys.stdin.readline
n,k = map(int,input().strip().split())

scores = [[0] for i in range(n)]

worst_rank = [-10000000000000]*n

top_score = -1000000000000000000000000000000000000
for i in range(k):
  nums = list(map(int,input().strip().split()))
  for j in range(n):
    if i == k-1:
      if scores[j][i] + nums[j] > top_score:
        top_score = scores[j][i] + nums[j]
    
    scores[j].append(scores[j][i] + nums[j])

  sorted_nums = sorted(nums,reverse=True)
  ranks = [sorted_nums.index(x)+1 for x in nums]

  for i in range(n):

    if ranks[i] > worst_rank[i]:
      worst_rank[i] = ranks[i]


top = [] 

for i in range(n):
  if scores[i][-1] == top_score:
    print("Yodeller " + str(i+1)+ " is the TopYodeller: score " + str(top_score) +", worst rank " + str(worst_rank[i]))




