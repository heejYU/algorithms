# 풀이 실패 -> 기존 코드 이해로 진행
# https://night-knight.tistory.com/entry/백준10799-쇠막대기-python-파이썬
ir= input()
stack=[]
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else :
        if ir[i-1]=="(":
            stack.pop()
            cnt+=len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.
            
        else :
            stack.pop()
            cnt+=1 # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.
print(cnt)