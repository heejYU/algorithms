def mult(mat1, mat2, result):
    for n in range(N):
        for k in range(K):
            for m in range(M):
                result[n][k] += mat1[n][m] * mat2[m][k]


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] # list()임. list[]가 아님.

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

result = [[0]*K for _ in range(N)]

mult(A, B, result)

for row in result:
    print(*row)  # * 넣어서 대괄호 없이 출력되게 함