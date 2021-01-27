# 부품 찾기
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())                            # 5
parts = list(map(int, input().split()))     # 8 3 7 9 2

parts.sort()

m = int(input())                            # 3
check = list(map(int, input().split()))     # 5 7 9

for target in check:
    result = binary_search(parts, target, 0, len(parts) - 1)
    if result is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
