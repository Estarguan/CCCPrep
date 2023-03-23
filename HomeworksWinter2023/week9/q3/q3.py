import sys
input = sys.stdin.readline

locations = ["HOME"]
dir = []
line = input().strip()
while line != "SCHOOL":
    if line == "R":
        dir.append("LEFT")
    elif line == "L":
        dir.append("RIGHT")
    else:
        locations.append(line)
    line = input().strip()
for i in range(len(locations)-1,-1,-1):
    if locations[i] != "HOME":
        print("Turn",dir[i],"onto",locations[i],"street.")
    else:
        print("Turn",dir[i],"into your HOME.")