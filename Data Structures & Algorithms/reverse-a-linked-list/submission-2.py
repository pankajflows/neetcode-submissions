# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # if not curr:
        #     return
        # if not curr.next:
        #     return curr
        # nex = curr.next

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        # curr.next = prev

        return prev