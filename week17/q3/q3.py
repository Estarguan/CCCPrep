import sys
input = sys.stdin.readline

letters=['A','B','C','D','E']
n = int(input())
code = []
for i in range(5):
	code.append(input().split())
for i in range(n):
	gift = input().strip()
	ans = ''
	for i in range(len(gift)-1):
		if gift[i] in letters:
			ans += code[letters.index(gift[i])][int(gift[i+1]) -1]
		elif gift[i].isalpha():
			ans += gift[i]
	print(ans)
