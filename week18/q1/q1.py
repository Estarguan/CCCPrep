line = input() #AFB+8HC-4

for i,v in enumerate(line):
    if v.isalpha():
        print(v, end="")
    else:
        if v.isdigit():
            continue
        if v == '+':
            print(" tighten ", end="")
        elif v == "-":
            print(" loosen ", end="")
        for j in range(i+1,len(line)):
            if line[j].isdigit():
                print(line[j],end="")
            else:
                print()
                break