# 문자열 압축

s = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
    ]

def solution(s):
    # 최소 길이의 압축 문자열 길이 저장
    min_len = len(s)
    # 비교 문자열 i
    for i in range(1, len(s) // 2 + 1):
        # 가능한 압축 문자열 저장
        res = ''
        first = s[0:i]
        # 중복되는 수
        cnt = 1
        for j in range(i, len(s), i):
            second = s[j:i + j]
            if first == second:
                cnt += 1
            else:
                res += (str(cnt) + first) if cnt >= 2 else first
                first = second
                cnt = 1
        # 반복문 이후 남은 문자열에 대해 추가
        res += (str(cnt) + second) if cnt >= 2 else second
        min_len = min(min_len, len(res))
    return min_len
        
for x in s:
    print(solution(x))
    
# 입력 예시
# aabbaccc
# 출력 예시
# 7

# 입력 예시
# ababcdcdababcdcd
# 출력 예시
# 9

# 입력 예시
# abcabcdede
# 출력 예시
# 8

# 입력 예시
# abcabcabcabcdededededede
# 출력 예시
# 14

# 입력 예시
# xababcdcdababcdcd
# 출력 예시
# 17
