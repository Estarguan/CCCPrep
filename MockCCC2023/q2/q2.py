n = int(input())
place = input()
if place.find("E") == -1:
    print(-1)
else:
    print(abs(place.find("Y") - place.find("E")))
