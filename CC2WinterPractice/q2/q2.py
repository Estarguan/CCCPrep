n = int(input())
if n >= 1000:
    cows = "moo"*1000
else:
    cows = "moo"*n
print("yes" if input() in cows else "no")