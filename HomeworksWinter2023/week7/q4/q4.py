import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
psa = [nums[0]]
for i in range(1,n):
    psa.append(psa[i-1]+nums[i])
for i in range(1,len(psa)):
    if psa[-1]-psa[i-1] == psa[i-1]:
        print(i)
        break
else:
    print("Andrew is sad.") 