text = input()
newText = ""
sentences = []
startIdx = 0
for i in range(len(text)):
  if text[i].isalpha() or text[i].isnumeric() or text[i] == " " or text[i] == "." or text[i] == "!" or text[i] == "?":
    newText += text[i]
  if text[i] == "'" or text[i] == "/" or text[i] == "-":
    newText += " "
text = newText

for i in range(len(text)):
  if text[i] == "." or text[i] == "!" or text[i] == "?":
    sentences.append(text[startIdx:i+1].split())
    startIdx = i+1

message = input().split()
ans = ""

for i in message:
  try:
    sentence,word,char = map(int,i.split("."))
    print(sentence,word,char)
    #sentences[sentence-1][word-1]
    i = 0
    realI = 0
    while realI != char:
      if sentences[sentence-1][word-1][i].isalpha() or sentences[sentence-1][word-1][i].isnumeric():
        i+= 1
        realI += 1
      else:
        i+= 1
    ans += sentences[sentence-1][word-1][i-1]
  except:
    ans += " "
    
print(ans)