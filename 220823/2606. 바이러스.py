from collections import deque
from sys import stdin

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(root):
    q = deque()
    q.append(root)
    visited = [0 for _ in range(n + 1)]
    visited[root] = 1

    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

    return sum(visited) - 1


print(bfs(1))