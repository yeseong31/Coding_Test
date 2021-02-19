# 치킨 배달

from itertools import combinations

# '도시의 치킨 거리'를 구하는 함수
def chicken_distance(s):
    result = 0
    for hx, hy in house:
        # '최단 도시 치킨 거리'를 구함
        dist = 1e9
        for sx, sy in s:
            dist = min(dist, abs(hx - sx) + (abs(hy - sy)))
        result += dist
    return result
                       
n, m = map(int, input().split())
# 집 좌표, 치킨집 좌표
house, chicken = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))
                       
# 도시에 있는 치킨집 중 M개를 고르는 경우
select = list(combinations(chicken, m))

dist = 1e9
for s in select:
    dist = min(dist, chicken_distance(s))

print(dist)
