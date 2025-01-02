# 동적 계획법 - 테이블화
'''
1. 인접한 집과의 색 다름
2. 그중 가장 작은 비용을 가지는 색 선택
3. 비용을 모두 더함
'''

# 입력 받기
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
# 행 : 각 집 / 열 : 순서대로 RGB
dp = [[0] * 3 for _ in range(N)]

# 첫 번째 집 비용 초기화
dp[0][0] = costs[0][0]  # 빨강
dp[0][1] = costs[0][1]  # 초록
dp[0][2] = costs[0][2]  # 파랑

# DP 테이블 채우기
for i in range(1, N):
    # i+1 번째 집을 RGB로 칠했을 때, 그 이전까지의 비용을 모두 더한 값을 저장
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])  # i가 빨강일 때 i-1은 초록 또는 파랑 
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])  # 초록
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])  # 파랑

# 최소 비용 출력
result = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
print(result)