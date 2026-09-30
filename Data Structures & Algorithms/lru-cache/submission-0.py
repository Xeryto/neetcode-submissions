class Node:
    def __init__(self, key: int, parent = None, child=None):
        self.key = key
        self.parent = parent
        self.child = child

class DoubleLinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    def add(self, node):
        self.head.parent = node
        node.child = self.head
        self.head = self.head.parent

    def deleteLast(self):
        evictedKey = self.tail.key
        self.tail = self.tail.parent
        self.tail.child.parent = None
        self.tail.child = None
        return evictedKey
    
    def delete(self, node):
        evictedKey = node.key
        child = node.child
        node.child = None
        node = node.parent
        node.child.parent = None
        node.child = child
        child.parent = node
        return evictedKey

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.usedCapacity = 0
        self.ll = None

    def refreshNode(self, node):
        if node.child == None:
            self.ll.add(self.cache[self.ll.deleteLast()][1])
        else:
            self.ll.add(self.cache[self.ll.delete(node)][1])

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.usedCapacity > 1 and not self.ll.head.key == key:
                self.refreshNode(self.cache[key][1])
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            if self.usedCapacity > 1 and not self.ll.head.key == key:
                self.refreshNode(self.cache[key][1])
            self.cache[key] = (value, self.cache[key][1])
            return
        if not self.ll:
            head = Node(key)
            self.ll = DoubleLinkedList(head)
            self.cache[key] = (value, head)
            self.usedCapacity+=1
            return
        if self.usedCapacity < self.capacity:
            node = Node(key)
            self.cache[key] = (value, node)
            self.ll.add(node)
            self.usedCapacity+=1
            return
        node = Node(key)
        self.cache[key] = (value, node)
        self.ll.add(node)
        del self.cache[self.ll.deleteLast()]