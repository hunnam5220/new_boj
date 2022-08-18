from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
prime = [1 for x in range(1001)]
prime[0], prime[1] = 0, 0
ans = 0


def get_prime():
    for i in range(2, 1001):
        if prime[i] == 1:
            temp = i
            while temp + i <= 1000:
                temp += i
                prime[temp] = 0


get_prime()
for i in arr:
    ans += 1 if prime[i] else 0
print(ans)