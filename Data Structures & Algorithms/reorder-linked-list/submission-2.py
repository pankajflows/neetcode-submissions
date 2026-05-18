# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList2(self, head: Optional[ListNode]) -> None:
        # naive mixing using O(n) space recursion, incomplete solution
        p1 = head
        p2 = head

        def visit(p):
            nonlocal p1, n
            if not p:
                return
            visit(p.next)

            n.next = p1
            n = n.next
            n.next = p
            p1 = p1.next
            


        empty_start = n = ListNode()
        visit(head)
        head = empty_start.next

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # splitting list into two
        slow = head
        fast = head
        even_slower = None
        while fast and fast.next:
            even_slower = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        even_slower.next = None

        l1 = head
        l2 = mid

        # reversing l2
        def reverseList(n):
            prev = None
            curr = n

            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex

            return prev

        l2 = reverseList(l2)

        # join linkedlists
        dummy = d = ListNode()
        c = 1
        while l1 and l2:
            if c % 2 == 0:
                d.next = l2
                l2 = l2.next
            else:
                d.next  = l1
                l1 = l1.next
            d = d.next
            c += 1

        d.next = l1 if l1 else l2

        head = dummy.next


