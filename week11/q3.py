import sys
input = sys.stdin.readline

k = int(input().strip())
first_row = [["*"*k,"x"*k, "*"*k]]*k
for i in first_row:
    print("".join(i))
second_row = [[" "*k,"x"*(k*2)]]*k
for i in second_row:
    print("".join(i))
third_row = [["*"*k," "*k, "*"*k]]*k
for i in third_row:
    print("".join(i))
