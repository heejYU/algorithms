# 참고한 코드: https://velog.io/@cindy0857/백준-1992번-쿼드트리-Python-파이썬

N = int(input())
video = [list(map(int, input().strip())) for _ in range(N)] #.split()이면 런타임 오류

def quadtree(n, vlist):
    s = 0
    for l in vlist:
        s += sum(l)
    
    if s == n**2:
        return '1'
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree(half,[l[:half] for l in vlist[:half]])
    temp += quadtree(half,[l[half:] for l in vlist[:half]])
    temp += quadtree(half,[l[:half] for l in vlist[half:]])
    temp += quadtree(half,[l[half:] for l in vlist[half:]])
    temp += ')'
    
    return temp

print(quadtree(N, video))


# 효민님 코드
'''
n = int(input())
video = [list(map(int, input().strip())) for _ in range(n)]

def quad_tree(x, y, size):
    # 현재 영역의 첫 번째 픽셀의 값
    current_color = video[x][y]

    # 현재 영역에서 첫 픽셀의 값과 나머지 모든 픽셀의 값이 동일한지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != current_color:
                # 색이 다른 경우, 4분할하여 quad_tree 함수 재귀 호출 - 이런식으로 문제를 분할해서 반복적으로 풀이
                new_size = size // 2
                return "(" + \
                    quad_tree(x, y, new_size) + \
                    quad_tree(x, y + new_size, new_size) + \
                    quad_tree(x + new_size, y, new_size) + \
                    quad_tree(x + new_size, y + new_size, new_size) + \
                    ")"

    # 모든 값이 동일하면 해당 픽셀의 값 반환
    return str(current_color)

# 출력
print(quad_tree(0, 0, n))
'''