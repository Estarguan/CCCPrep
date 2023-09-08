letters = sorted(list(input()))


def permute(current,letters):
    if len(letters) == 0:
        print("".join(current))
    else:
        for i in letters:
            a = current.copy()
            a.append(i)
            b = letters.copy()
            b.remove(i)
            permute(a,b)

permute([],letters)
