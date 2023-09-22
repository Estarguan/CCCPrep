for _ in range(10):
    wash = 0
    events = {}
    n,m,d = map(int,input().split())
    shirt_count = n
    event = list(map(int,input().split()))
    for i in range(m):
        events[event[i]] = events.get(event[i],0) + 1
    for i in range(d):
      if n == 0:
        wash += 1
        n = shirt_count
      n -= 1
      if i+1 in events:
        shirt_count += events[i+1]
        n += events[i+1]
    print(wash)
