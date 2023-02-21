n = int(input())
s, t = 0, 0
for i in range(n):
    line = input().lower()
    for i in line:
        if i == "s":
            s+=1
        elif i == "t":
            t+=1
if s > t:
    print("French")
elif s < t:
    print("English")
else:
    print("French")
