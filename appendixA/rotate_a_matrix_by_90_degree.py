''' 2차원 리스트(행렬)를 90도 회전하는 메서드'''
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    col_length = len(a[0])

    result = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            result[c][row_length - 1 - r] = a[r][c]
    return result

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree(a))