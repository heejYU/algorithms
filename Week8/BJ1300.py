# 못 풀어서 코드 참고 & 분석으로 진행

N, K = map(int(), input().split())
start, end = 1, K

while start <= end :
    mid = (start + end) // 2

    temp = 0
    for i in range (1, N+1):
        temp += min(mid // i, N)

    if temp >= K :
        answer = mid
        end = mid -1

print(answer)
