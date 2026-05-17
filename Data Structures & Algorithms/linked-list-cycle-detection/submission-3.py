# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while head:
            if slow.next:
                slow = slow.next
                if fast.next and fast.next.next:
                    fast = fast.next.next
                else:
                    return False
            else:
                return False
            if slow is not None and slow == fast:
                return True
        return False