import sys
input = sys.stdin.readline

for n in range(10):
    st = set()
    for i in range(int(input())):
        s = input().lower()
        at = s.index("@")
        period = s[:at].replace(".", "")
        second = s[at:]
        user = period.split("+")[0]
        st.add(user+second)
    print(len(st))
