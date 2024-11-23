# 기존 코드를 이해하는 방식으로 진행
# https://velog.io/@rkdalstn7221/%EB%B0%B1%EC%A4%80-16987-%EA%B3%84%EB%9E%80%EC%9C%BC%EB%A1%9C-%EA%B3%84%EB%9E%80%EC%B9%98%EA%B8%B0-Python

def check(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt


def solution(depth, arr):
    global answer
    if depth == n:
        answer = max(answer, check(arr))
        return
    # 현재 들고있는 계란이 깨졌을때
    if arr[depth][0] <= 0:
        solution(depth + 1, arr)
    else:
        isBroken = True
        for i in range(n):
            if depth != i and arr[i][0] > 0:
                isBroken = False
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                solution(depth + 1, arr)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        if isBroken:
            solution(n, arr)


n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]
answer = 0
solution(0, egg)
print(answer)