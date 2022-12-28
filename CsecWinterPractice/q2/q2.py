i = int(input())
for i in range(i):
    s = input()
    for j in range(len(s)-1):
        if s[j] == s[j+1]:
            s = s.replace(s[j],".",1)
    print(len(s)-(s.count("A")+s.count("B")))
