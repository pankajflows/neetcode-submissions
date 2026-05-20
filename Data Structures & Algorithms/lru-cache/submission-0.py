class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.root = None
        self.hashmap = dict()

    def insert_forward(self, node):
        if not self.root:
            self.root = node
            node.next = node
            node.prev = node
            self.length += 1
            return

        old_tail = self.root.prev

        old_tail.next = node
        node.prev = old_tail

        node.next = self.root
        self.root.prev = node

        self.root = node
        self.length += 1
    
    def remove(self, node):
        if self.length == 1:
            self.root = None
        elif node == self.root:
            self.root = node.next

        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        

    def get(self, key: int) -> int:
        if self.length <= 0 :
            return -1
        
        # find them
        found = self.hashmap.get(key, None)
        if not found:
            return -1

        # pop them
        self.remove(found)

        # put them forward
        self.insert_forward(found)

        # return it
        return found.val
        

    def put(self, key: int, value: int) -> None:
        found = self.hashmap.get(key, None)
        if found:
            # pop
            self.remove(found)
            found.val = value
        else:
            # create new
            found = self.hashmap[key] = Node(key, value)

        # insert at front
        self.insert_forward(found)

        # check if it exceeds
        if self.length > self.capacity:
            to_death = self.root.prev
            self.remove(to_death)
            self.hashmap.pop(to_death.key)
        
