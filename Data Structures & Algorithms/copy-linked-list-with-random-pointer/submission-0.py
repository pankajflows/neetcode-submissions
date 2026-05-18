"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Making map with copies
        hashmap = {None: None}
        n = head
        while n:
            hashmap[n] = Node(x=n.val)
            n = n.next

        # linking
        n = head
        while n:
            hashmap[n].next = hashmap[n.next]
            hashmap[n].random = hashmap[n.random]
            n = n.next

        return hashmap[head]

        