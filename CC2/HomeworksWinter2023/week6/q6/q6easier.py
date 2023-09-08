import itertools

s = input()

lst = ["".join(perm) for perm in itertools.permutations(s)]
lst.sort()
for word in lst:
    print(word)