from sys import stdin
stack = []

for _ in range(int(stdin.readline())):
    data = stdin.readline().split()
    if len(data) > 1:
        stack.append(int(data[1]))

    else:
        if data[0] == 'pop':
            print(stack.pop() if stack else -1)

        elif data[0] == 'size':
            print(len(stack))

        elif data[0] == 'empty':
            print(0 if stack else 1)

        elif data[0] == 'top':
            print(stack[-1] if stack else -1)