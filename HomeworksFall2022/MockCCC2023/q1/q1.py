B,K,N,R,P = map(int,input().split())
B = B -K - 2*N - (R%40)
if B < 0:
    B = 0
print(B*4*P)