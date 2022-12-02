increase_rate=float(input())
startyear=int(input())
startpop=int(input())
endyear=int(input())
rate = 1 + increase_rate/100.0
numyear=endyear-startyear
total = startpop*pow(rate, numyear)
print('%.0f' % total)
