def dnc(mat, size):
    global count
    first_value = mat[0][0]

    for i in range(size):
        for j in range(size):
            if mat[i][j] != first_value:
                half = size // 2
                # [row[열 범위] for row in mat[행 범위]], size
                dnc([row[:half] for row in mat[:half]],half) #1
                dnc([row[half:] for row in mat[:half]],half) #2
                dnc([row[:half] for row in mat[half:]],half) #3
                dnc([row[half:] for row in mat[half:]],half) #4
                return   # 함수 종료
            
    if first_value == 0:
        count[0] += 1
    else:
        count[1] += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count = [0,0]  # 색종이 개수 저장
dnc(paper, N)

print(count[0])
print(count[1])