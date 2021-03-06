# 바닥 공사 (p.223)

# 이 문제 또한 마찬가지로 다이나믹 프로그래밍의 기초 예제에서 빠질 수 없는 타일링 문제 유형이다.
# 이 문제 또한 그림으로 그려서 생각하면 어렵지 않게 풀 수 있다.

#     1. 왼쪽부터 (i - 1)까지 길이가 덮개로 이미 채워져 있으면 2 x 1의 덮개를 채우는 하나의 경우밖에 존재하지 않는다.
#     2. 왼쪽부터 (i - 2)까지 길이가 덮개로 이미 채워져 있으면 1 x 2 덮개 2개의 경우, 2 x 2 덮개 1개의 경우, 이렇게 2가지 경우가 있다.
#        (1 x 1 덮개 2개의 경우는 1번에서의 과정과 겹치는 부분이 있음)
# 또한 이 문제 역시 왼쪽부터 N - 2 미만의 길이에 대해서는 고려할 필요가 없다.
# 왜냐하면 사용할 수 있는 덮개의 형태가 최대 2 x 2의 직사각형 형태이기 때문이다.
#     a(i) = a(i - 1) + 2 * a(i - 2)

# ---------------------------------------------------------------------------------------------------------------------
# 정수 N 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic programming) 진행(보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])