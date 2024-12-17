S = input()
T = input()

# T를 S로 만들 수 있는지 역추적
while len(T) > len(S):
    if T[-1] == 'A':   # T의 마지막 문자가 A라면
        T = T[:-1]     # 마지막 문자 제거
    elif T[-1] == 'B': # T의 마지막 문자가 B라면
        T = T[:-1]     # 마지막 문자 제거
        T = T[::-1]    # 문자열 뒤집기

# 최종적으로 S와 T가 같은지 확인
if T == S:
    print(1)
else:
    print(0)