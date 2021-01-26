# 음료수 얼려 먹기

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]

ice_frame = []
for i in range(n):
    ice_frame.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if ice_frame[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j):
                result += 1

print(result)

# 입력 예시
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# 출력 예시
# 8
