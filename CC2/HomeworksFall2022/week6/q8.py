import sys
input = sys.stdin.readline

N = int(input().strip())
str = input().strip()

for k in range(1, N):
    for i in range(N-k+1):
        temp = str[i:i+k]
        location = 0
        for j in range(2):
            location = s[location.find(temp)]
            if location == -1:
                break
            location += 1
        else:
            break
    else:
        print(k)
        break
else:
    print(N)
