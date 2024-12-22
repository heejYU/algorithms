N = int(input())
paper = []
for i in range(N):
    row = [int(ch) for ch in input().rstrip()]

def find(N, paper):
    cnt = [] #[0]은 0, [1]은 1, [2]==[-1]는 -1 count
    # -1, 1의 개수가 같을 때와 0만 있을 때를 어떻게 구분할 것인가?
    is_uniform = True
    first_value = paper[0][0]
    for row in paper:     # paper 행렬에 다른 값이 있으면 break
        for element in row:
            if element != first_value:
                is_uniform = False
                break
        if not is_uniform:
            break
    else:                # paper 행렬에 다른 값이 없을 경우 실행
        if first_value == -1:
            cnt[-1] += 1
        elif first_value == 0:
            cnt[0] += 1
        else:
            cnt[1] += 1
    '''
    1 2 3
    4 5 6
    7 8 9
    '''
    one_third = N // 3  # 9등분한 종이(행렬)의 크기
    # find(행열의 크기, [elem[열 범위를 슬라이싱] for elem in paper[행 범위를 슬라이싱]])
    find(one_third, [elem[:one_third] for elem in paper[:one_third]])   # 1
    find(one_third, [elem[one_third : one_third*2] for elem in paper[:one_third]])   # 2
    find(one_third, [elem[:one_third*2] for elem in paper[:one_third]])   # 3

    find(one_third, [elem[:one_third] for elem in paper[one_third : one_third*2]] )  # 4
    find(one_third, [elem[one_third : one_third*2] for elem in paper[one_third : one_third*2]])   # 5
    find(one_third, [elem[:one_third*2] for elem in paper[one_third : one_third*2]])   # 6
    
    find(one_third, [elem[:one_third] for elem in paper[one_third*2:]] )  # 7
    find(one_third, [elem[one_third : one_third*2] for elem in paper[one_third*2:]])   # 8
    find(one_third, [elem[:one_third*2] for elem in paper[one_third*2:]])   # 9
 


    return cnt

print(find(N, paper)[-1])
print(find(N, paper)[0])
print(find(N, paper)[1])