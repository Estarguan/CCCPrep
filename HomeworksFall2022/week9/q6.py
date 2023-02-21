import sys
input = sys.stdin.readline

open_brac = ("(", "[", "{")
close_brac = (")", "]", "}")

def check(string):
    open_list = []
    for letter in string:
        #is it a letter
        if letter not in open_brac and letter not in close_brac:
            continue
        #is it open or close
        if letter in open_brac:
                open_list.append(letter)
        else:
            #is our open_list empty
            if open_list == []:
                return "not balanced"
            #yea this part
            if open_brac[close_brac.index(letter)] != open_list[-1]:
                return "not balanced"
            else:
                    open_list.pop()
    if open_list != []:
        return "not balanced"
    else:
        return "balanced"

for i in range(5):
    string = input().strip()
    print(check(string))
