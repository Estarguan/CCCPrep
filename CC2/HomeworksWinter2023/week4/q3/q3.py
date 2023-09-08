import sys
input = sys.stdin.readline

correct = True
num_students = int(input())
line_2_names = input().split()
line_3_names = input().split()
groups = {}

for i in range(num_students):
    groups[line_2_names[i]] = line_3_names[i]
    groups[line_3_names[i]] = line_2_names[i]
for x in range(num_students):
    partner1 = groups[line_2_names[x]]
    partner2 = groups[line_3_names[x]]
    if partner1 == partner2:
        correct = False
    if groups[partner1] != partner2:
        correct = False

if correct:
    print("good")
else:
    print("bad")
