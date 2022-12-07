import sys
input = sys.stdin.readline

n = int(input())
count = n-1
lst = ["M","_"]
for i in range(n-2):
    lst.append("M")
for i in range(1, n):
    if i > 1:
        if lst[i] == "M":
            continue
        elif lst[i] == "_":
            if lst[i-2] == "_":
                lst[i] = "M"
                lst[i+1] = "_"

            else:
                if lst[i-2] != "M":
                    lst[i+1] = "_"
                    count -= 1
    else:
        lst[i+1] = "M"
        lst[i+2] = "_"
        count -=1


print(count)
for i in lst:
    print(i, end="")
#_MM_M
#_MM__

# 6
# MM_MM_
# 7
# _MM_MM_