from sys import stdin

while 1:
    s = stdin.readline().rstrip()
    if s == '0':
        break

    i = len(s) // 2
    if len(s) % 2 != 0:
        temp = s[i + 1:]
        if s[:i] == temp[::-1]:
            print('yes')
        else:
            print('no')
    else:
        temp = s[i:]
        if s[:i] == temp[::-1]:
            print('yes')
        else:
            print('no')