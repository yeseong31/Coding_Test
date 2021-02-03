# 팀 결성

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
    parent[i] = i

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

# ---------------------------------------------------------------------------------------------------------------------
# 전형적인 서로소 집합 알고리즘 문제
# N과 M의 범위가 최대 100000이므로 '경로 압축 방식'의 서로소 집합 자료구조를 이용해야 한다.
