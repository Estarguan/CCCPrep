changes = {
 '0':'O',
 '1':'l',
 '3':'E',
 '4':'A',
 '5':'S',
 '6':'G',
 '8':'B',
 '9':'g'
}
line = list(input())
for i in range(len(line)):
  if line[i] in changes:
    line[i] = changes[line[i]]
print(''.join(line))