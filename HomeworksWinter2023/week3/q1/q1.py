text = input()
s = list(input())
#[A,B,C,D,E]
cyclic = []
for i in range(len(s)):
    s.insert(0,s[len(s)-1])
    s.pop()
    cyclic.append("".join(s))
def checking(text, c):
    for i in c:
        if i in text:
            return "yes"
    else:
        return "no"
print(checking(text,cyclic))
