import sys
input = sys.stdin.readline 

for _ in range(10):
    R,T,A=input().strip().split()
    f1 = [0]*26
    for c in A:
        f1[ord(c)-ord('A')] += 1
    rule = {}
    for i in range(int(R)):
        x,y = input().strip().split()
        rule[x]=y
    fst,lst = A[0],A[-1]
    for i in range(int(T)):
        fst,lst = rule[fst][0], rule[lst][-1]
        f2=[0]*26
        for k,v in rule.items():
            for c in v:
                f2[ord(c)-ord("A")] += f1[ord(k)-ord("A")]
        f1 = f2[:]
    print(fst+lst,sum(f1))