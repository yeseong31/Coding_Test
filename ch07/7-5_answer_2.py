# 계수 정렬의 개념을 이용하여 문제를 풀 수도 있다.
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤에,
# 리스트의 인덱스에 직접 접근하여 특정한 번호의 부품이 매장에 존재하는지 확인하면 된다.

# N(가게의 부품 개수) 입력
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 학인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')