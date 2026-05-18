# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Going over the list in 2 iterations to decide nth
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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using fast and slow pointers
        dis = 0
        node = no = ListNode()
        node.next = head
        slow = node
        fast = node

        while fast:
            while dis <= n-1:
                dis += 1
                fast = fast.next
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next
        print(slow.val, fast)
        slow.next = slow.next.next if slow.next else None

        return no.next


















