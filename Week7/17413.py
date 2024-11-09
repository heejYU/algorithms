class Stack:
    def __init__(self):
        self.top = -1
        self.array = []

    def pop(self):
        if self.top == -1:
            return None  # 스택이 비었을 경우 None 반환
        self.top -= 1
        return self.array[self.top + 1]

    def push(self, item):
        self.top += 1
        if self.top < len(self.array):
            self.array[self.top] = item
        else:
            self.array.append(item)  # 배열 크기가 모자랄 경우 새로 추가

def reverse_word(S):
    P = ""
    stack = Stack()  # 스택 객체 생성
    i = 0  # i 변수 초기화

    while i < len(S):
        if S[i] == '<':  # '<'를 만나면
            while stack.top != -1:  # 스택에 요소가 있으면 pop하여 P에 추가
                P += stack.pop()
            while i < len(S) and S[i] != '>':  # '<'부터 '>'까지 그대로 P에 추가
                P += S[i]
                i += 1
            P += '>'  # '>' 추가
        elif S[i] == ' ':  # 공백을 만나면
            while stack.top != -1:  # 스택에 요소가 있으면 pop하여 P에 추가
                P += stack.pop()
            P += ' '  # 공백도 P에 추가
        else:
            stack.push(S[i])  # 스택에 문자 추가
        i += 1

    # 스택에 남아있는 문자를 모두 뒤집어서 추가
    while stack.top != -1:
        P += stack.pop()

    return P

# 입력 받기
S = input()
print(reverse_word(S))
