import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u','y']

count = 0
line = input().strip()
for i in line:
    if i in vowels:
        count += 1
        if count >= 2:
            print("good")
            break
else:
    print("bad")