# 동적 계획법 - 테이블화

# 입력 받기
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(n)]

# 첫 번째 집 비용 초기화
dp[0][0] = costs[0][0]  # 빨강
dp[0][1] = costs[0][1]  # 초록
dp[0][2] = costs[0][2]  # 파랑

# DP 테이블 채우기
for i in range(1, n):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])  # 빨강
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])  # 초록
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])  # 파랑

# 최소 비용 출력
result = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(result)