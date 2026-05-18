# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == 1:
            return None if n == 1 else head

        before_nth = length - n

        node = n = ListNode()
        node.next = head
        counter = -1
        while node:
            counter += 1
            print(counter, before_nth)
            if counter == before_nth:
                node.next = node.next.next
            node = node.next

        return n.next