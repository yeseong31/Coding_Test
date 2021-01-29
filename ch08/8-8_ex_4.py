# 효율적인 화폐 구성 (p.226)

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블
# 각 인덱스에 해당하는 값으로 10001을 설정한다.
# 1001은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미이다.
d = [10001] * (m + 1)

d[0] = 0
# 화폐 단위 개수만큼 반복
for k in array:
    for i in range(k, m + 1):
        d[i] = min(d[i], d[i - k] + 1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)