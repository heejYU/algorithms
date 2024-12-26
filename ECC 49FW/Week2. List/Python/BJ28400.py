N, K = map(int, input().split())
wheel = ['?'] * N

log = []
for i in range(K):
    S, ch = input().split()
    log.append((int(S),ch))
idx = 0
for i in range(K):
    idx = (idx + log[i][0]) % N
    if (wheel[idx] != '?' and wheel[idx] != log[i][1]) or (wheel[idx] == '?' and log[i][1] in wheel): # 알파벳 불일치 또는 중복
        N = 1
        wheel[0] = '!'
        break
    wheel[idx] = log[i][1]
for i in range(N):
    print(wheel[(idx-i) % N],end='')