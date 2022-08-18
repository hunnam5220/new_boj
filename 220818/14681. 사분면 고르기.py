x, y = int(input()), int(input())
if 0 < x and 0 < y:
    print(1)
elif 0 < x and 0 > y:
    print(4)
elif 0 > x and 0 < y:
    print(2)
else:
    print(3)