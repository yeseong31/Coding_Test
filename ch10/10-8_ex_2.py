# 도시 분할 계획

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = 1

edges = []
result = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

# ---------------------------------------------------------------------------------------------------------------------
# 전체 그래프에서 2개의 최소 신장 트리를 만들어야 하는 문제
# 최소한의 비용으로 2개의 신장 트리로 분할하는 방법은 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에
# '최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거'하는 것이다.
