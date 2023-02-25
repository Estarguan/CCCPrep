import sys
input = sys.stdin.readline

s = input().strip()
psa = [[0] * (len(s) + 1) for i in range(26)]
for i in range(1,len(s)+1):
    for j in range(26):
        psa[j][i] = psa[j][i-1]
    if s[i-1] != ' ':
        psa[ord(s[i-1]) - 97][i] += 1

for i in range(int(input())):
    l,r,c = input().strip().split()
    l,r,idx = int(l),int(r),ord(c)-97
    print(psa[idx][r] - psa[idx][l-1])