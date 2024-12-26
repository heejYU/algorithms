# reference: https://velog.io/@yje876/python백준분할정복-1780-종이의-개수
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def find(N, paper):
    result = [0,0,0] # 개수 저장 result[-1] = result[2]
    first_value = paper[0][0]
    all_same = True
    for row in paper:     # paper 행렬에 다른 값이 있으면 break
        for element in row:
            if element != first_value:
                all_same = False
                break
        if not all_same:
            break
    
    if all_same:
        result[first_value] += 1
        return result
    else:
        one_third = N // 3  # 9등분한 종이(행렬)의 크기
        # find(행열의 크기, [elem[열 범위를 슬라이싱] for elem in paper[행 범위를 슬라이싱]])
        for i in range(3):
            for j in range(3):
                sub_paper = [row[j * one_third:(j + 1) * one_third] for row in paper[i * one_third:(i + 1) * one_third]]
                find(one_third, sub_paper)
                '''
                9등분한 종이의 위치
                    123
                    456
                    789

                find(one_third, [elem[:one_third] for elem in paper[:one_third]])   # 1
                find(one_third, [elem[one_third : one_third*2] for elem in paper[:one_third]])   # 2
                find(one_third, [elem[one_third*2:] for elem in paper[:one_third]])   # 3

                find(one_third, [elem[:one_third] for elem in paper[one_third : one_third*2]] )  # 4
                find(one_third, [elem[one_third : one_third*2] for elem in paper[one_third : one_third*2]])   # 5
                find(one_third, [elem[one_third*2:] for elem in paper[one_third : one_third*2]])   # 6

                find(one_third, [elem[:one_third] for elem in paper[one_third*2:]] )  # 7
                find(one_third, [elem[one_third : one_third*2] for elem in paper[one_third*2:]])   # 8
                find(one_third, [elem[one_third*2:] for elem in paper[one_third*2:]])   # 9

                '''
    return result

result = find(N, paper)
print(result[-1])
print(result[0])
print(result[1])