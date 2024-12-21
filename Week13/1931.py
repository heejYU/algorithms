#input
N = int(input())
meetings = [] # 회의의 (시작, 종료) 시간
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

'''
end time을 기준으로 오름차순 정렬.
현재 회의를 다음과 같이 설정하고 첫 번째 회의(end time이 작은)를 먼저 담는다. meeting = 첫 번째 회의
두 번째 회의부터, 즉 end time이 작은 회의부터 순차적으로 아래 조건을 충족하는지 탐색.
첫 번째 end time <= start time 조건을 충족하는 회의를 I라 하면
그 다음 회의 meeting = I
이를 해당 조건을 충족하는 회의가 없을 때까지 반복, 즉 시행 후에도 meeting의 값이 여전하면 종료
'''
# end time(튜플의 두 번째 요소)를 기준으로 회의 sorting
meetings.sort(key=lambda x: (x[1],x[0]))
endTime = 0  # 첫 번째 회의는 확정
count = 0              # 회의 개수
for start, end in meetings:
    if start >= endTime:  # 확정된 회의의 끝나는 시간이 다음 회의의 시작 시간보다 작거나 같으면
        endTime = end         # 다음 회의를 확정한다.
        count += 1

print(count)