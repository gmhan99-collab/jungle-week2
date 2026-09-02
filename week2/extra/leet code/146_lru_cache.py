class LRUCache: # doubly linked list

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node("","") 
        self.tail = Node("","")
        self.head.next = self.tail
        self.tail.prev = self.head

        # o(1) 복잡도로 실행되어야 함
    def find(self, key) -> Node:# data가 cache에 있는지 판단
        node = self.head.next
        while node != self.tail:
            if node.key == key:
                return node
            node = node.next
        return None
    
    def get(self, key: int) -> int:
        if self.find(key) != None :
            newnode = self.find(key)
            self.remove(self.find(key))
            self.prepend(key, newnode.value)
            return newnode.value
        else: return -1
            # 찾은 데이터 담긴 노드 떼서 앞에다 붙이기

        
    def put(self, key: int, value: int) -> None:
        if not self.find(key):
            self.prepend(key, value)
        else:
            self.remove(self.find(key)) 
            self.prepend(key, value)
        if self.cachelen() > self.capacity:
            self.removeTail()
         # 넣을 데이터 앞에다 붙이기, 길이 초과하면 맨 뒤에서 자르기
        
    def remove(self, node): # prev 노드의 next 에 next를, next 노드의 prev에 prev넣기
            node.prev.next = node.next
            node.next.prev = node.prev

    def prepend(self, key, value):

        '''
        1. head.next의 prev에 newnode
        2. newnode의 next 에 head.next
        3. newnode의 prev에 head
        4. head.next에 newnode
        '''
        newnode = Node(key, value)
        self.head.next.prev = newnode
        newnode.next = self.head.next
        newnode.prev = self.head
        self.head.next = newnode

    def cachelen(self):
        length = 0
        node = self.head.next
        while node != self.tail:
            length += 1
            node = node.next
        return length
    def removeTail(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

class Node :

    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    # Least Recently Used Cache
    # doubly linked list 로 구현한다고 함.
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)