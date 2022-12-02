import sys
input = sys.stdin.readline

ant, eye = int(input()),int(input())
if (ant >= 3 and eye <= 4):
    print("TroyMartian")
if (ant <= 6 and eye >= 2):
    print("VladSaturnian")
if (ant <= 2 and eye <= 4):
    print("GraemeMercurian")
