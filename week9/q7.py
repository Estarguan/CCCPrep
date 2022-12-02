import sys
input = sys.stdin.readline


for _ in range(int(input().strip())):
    cars,branch, lake = [" "], [" "], 1
    for car in range(int(input().strip())):
        cars.append(int(input().strip()))
    while cars[-1] != 1:
        branch.append(cars[-1])
        cars.pop()
    cars.pop()
    while cars != [" "] or branch != [" "]:
        if branch == [" "]:
            if cars[-1] == lake+1:
                lake += 1
                cars.pop()
            else:
                branch.append(cars[-1])
                cars.pop()
        if cars == [" "] and branch[-1] != lake+1:
            print("N")
            break
        elif cars[-1] != lake+1 and branch[-1] != lake+1:
            branch.append(cars[-1])
            cars.pop()
        elif cars[-1] != lake+1 and branch[-1] == lake+1:
            lake += 1
            branch.pop()
        elif cars[-1] == lake+1 and branch[-1] != lake+1:
            lake += 1
            cars.pop()
    if branch == [" "]:
        print("Y")
