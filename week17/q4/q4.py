import sys
input = sys.stdin.readline

hunger,apples,wait,bar = int(input()),int(input()),int(input()),0
bar = hunger if apples > hunger else apples
bar = 0 if bar - wait < 0 else bar-wait
print(bar)
