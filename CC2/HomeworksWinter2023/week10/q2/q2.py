import itertools
import sys
input = sys.stdin.readline

score = int(input())
line = input().strip()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = [''.join(i) for i in itertools.product(alphabet, repeat = 4)]
for i in words:
    count = 0
    for j in range(4):
        if i[j] != line[j]:
          distance_forward = ord(i[j]) - ord(line[j])
          distance_backward = ord(line[j]) - ord(i[j])
          
          if distance_forward < 0:
              distance_forward += 26
          
          if distance_backward < 0:
              distance_backward += 26
          
          count += min(distance_forward, distance_backward)
    if count <= score:
        print(i)
          