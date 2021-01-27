# 떡볶이 떡 만들기

n, m = map(int, input().split())
array = list(map(int, input().split()))

height = 0

# 이진 탐색 시작
start = 0
end = max(array)
while start <= end:
    total = 0   # 잘린 떡의 총 길이
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += (i - mid)
    # 잘린 떡의 길이가 충분치 않다면 mid를 왼쪽으로 더
    if total < m:
        end = mid - 1
    # 잘린 떡의 길이가 충분하다면(넘친다면) mid를 오른쪽으로 더
    else:
        start = mid + 1
        height = mid    # 길이 저장

print(height)