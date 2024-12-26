# 백준 1080 행렬
def flip(mat, row, column):
    for i in range(3):
        for j in range(3):
            mat[row+i][column+j] = 1- mat[row+i][column+j]
      
# 입력
count = 0
A = []
B = []
N, M = map(int, input().split())
for _ in range(N):
    row = input().strip()
    A.append([int(char) for char in row])
for _ in range(N):
    row = input().strip()
    B.append([int(char) for char in row])

# 뒤집기 수행. M, N이 3보다 작을 시 수행되지 않음
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(A,i,j)
            count += 1
if A != B:
    count = -1

print(count)