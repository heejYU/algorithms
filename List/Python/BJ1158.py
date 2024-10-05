class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, node):
        self.head = node
        node.link = self.head
    def size(self):
        if self.head is None:
            return 0
        node = self.head # self.head로 노드를 지정했는데 while문 조건에 not self.head를 걸어서 while 문 실행이 안 됨
        size = 1
        while True:
            node = node.link
            size += 1
            if node.link is self.head: break;# is는 객체 참조 비교 == 은 값 비교
        return size
    def popNode(self, pos):
      if self.head is None:
          return None
      if pos < 0:
          return None
      node = self.head
      i = 0
      while i < pos:
          if (i == pos-1):
            previous = node
          node = node.link
          i += 1
      # node 삭제
      previous.link = node.link
      return node

# 입력
N, K = map(int, input().split())
# 1부터 N까지의 수로 된 리스트 llst
llst = CircularLinkedList()
for i in range(N):
    llst.append(Node(i))
# K번째 사람 제거하기
# 순서대로 리스트에 저장
permt = ""
print(llst.size())
while (llst.size() > 1):
  # K번째 노드 pop
  node = llst.popNode(K)
  permt += str(node.data)+', '
# print
print(f"<{permt[:-2]}>")
