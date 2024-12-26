import sys

# 임의의 위치에서 상어와의 안전 거리 찾기
def safe(pos, sharks):  # 임의의 좌표 pos = (i,j), shark = (n,m)
    dist = []
    for shark in sharks :
        dr = abs(pos[0] - shark[0]) # pos와 shark 행 좌표의 차이
        dc = abs(pos[1] - shark[1])
        dist.append(abs(dr-dc) + min(dr, dc))
    return min(dist)
    
# 최대안전거리 찾기
def find_max_safe_dist(N,M,sharks):
    max_safe = 0
    for n in range (N):
        for m in range(M):
            safe_dist = safe((n, m),sharks)
            max_safe = max(safe_dist,max_safe)
    return max_safe

# 첫째 줄 입력
N, M = map(int, input().split())

# 상어 위치 저장
sharks = []  # [pos(shark1), pos(shark2)] = [(0,1),(3,5)]
for row_idx, line in enumerate(sys.stdin):
    row = list(map(int,line.strip().split()))
    for col_idx, value in enumerate(row):
        if value == 1:
            sharks.append((row_idx, col_idx))

max_safe = find_max_safe_dist(N,M,sharks)

print(max_safe)