# 미로 탈출
from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

distance = miro

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖이면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 상, 하, 좌, 우 비교
            if miro[nx][ny] == 1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
    return distance[n-1][m-1]


print(bfs(0, 0))

# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 출력 예시
# 10