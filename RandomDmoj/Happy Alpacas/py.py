n,x = map(int,input().split())

if (n-x) % 2 != 0:
  print(-1)
elif n == x:
	ans = ''
	for i in range(n):
		ans += '1 '
	print(ans.strip())
else:
	ans = []
	for i in range(x+1):
		ans.append('1 ')
	for i in range(n-x-1):
		if i % 2 == 0:
			ans.append('0 ')
		else:
			ans.append('1 ')
	if len(ans) > n:
		print(-1)
	else:
		print(("".join(ans)).strip())