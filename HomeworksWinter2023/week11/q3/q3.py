n = int(input())
cases = [100,500,1000,5000,10_000,25_000,50_000,100_000,500_000,1_000_000]
fin_cases = cases.copy()
for i in range(n):
	case = int(input())
	fin_cases.remove(cases[case-1])
offer = int(input())
if sum(fin_cases)/len(fin_cases) > offer:
	print("no deal")
else:
	print("deal")