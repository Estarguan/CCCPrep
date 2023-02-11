import sys
input = sys.stdin.readline

n = int(input())
tot = 0

def fun(prev,sum,sol):
    global tot
    if sum == n:
        print(sol)
        tot += 1
        return
    for cur in range(prev,n-sum+1):
        fun(cur,sum+cur,sol + '+' + str(cur))
for i in range(1,n//2+1):
    fun(i,i,str(n) + '=' + str(i))
print('total='+str(tot))
