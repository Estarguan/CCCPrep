import sys
input = sys.stdin.readline 

s = input().strip()
zeros = [0 for i in range(len(s))]
ones = [0 for i in range(len(s))]
for i in range(len(s)):
	try:
		ones[i] = ones[i-1]
	except:
		continue
	try:
		zeros[i] = zeros[i-1]
	except:
		continue
	if s[i] == '0':
		zeros[i] += 1
			
	elif s[i] == '1':
		ones[i] += 1
q = int(input())

for i in range(q):
	x,y,z = map(int, input().strip().split())
	if z == 0:
		try:
			print(zeros[x-1:].index(y) + 1)
		except:
			print(-1)
	elif z == 1:
		try:
			print(ones[x-1:].index(y) + 1)
		except:
			print(-1)