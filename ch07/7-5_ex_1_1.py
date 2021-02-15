# 부품 찾기

from bisect import bisect_left, bisect_right

n = int(input())
parts = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

parts.sort()
for check in checks:
    left = bisect_left(parts, check)
    right = bisect_right(parts, check)
    print('no' if left - right == 0 else 'yes')
