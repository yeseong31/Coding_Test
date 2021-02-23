# 18352 - 특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline

# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시 x
n, m, k, x = map(int, input().split())
# 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# 거리 테이블
distance = [-1] * (n + 1)
distance[x] = 0

# bfs
q = deque([x])
while q:
    v = q.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            q.append(i)

c = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        c = True
if not c:
    print(-1)
