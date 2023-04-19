import sys
input = sys.stdin.readline 
l = 1
r= 2 * 10 ** 9
m = (l+r)//2

while True:
	print(m)
	sys.stdout.flush()
	result = input().strip()
	if result == "OK":
		sys.exit()
	elif result == "FLOATS":
		r = m-1
		m = (l+r)//2
	else:
		l = m+1
		m = (l+r)//2
		