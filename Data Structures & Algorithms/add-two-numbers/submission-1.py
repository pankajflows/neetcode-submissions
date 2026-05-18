# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = a = None
        while l1 and l2:
            # print("adding", l1.val, l2.val)
            temp = l1.val + l2.val + carry
            dsum = temp % 10
            carry = 1 if temp > 9 else 0

            if ans is None:
                # print("first sum is", dsum)
                ans = a = ListNode(dsum)
            else:
                # print("sum is", dsum)
                ans.next = ListNode(dsum)
                ans = ans.next

            l1 = l1.next
            l2 = l2.next


        # If one list exhausts but other doesn't
        print("rem", l1, l2)
        l_rem = l1 if l1 else l2
        while l_rem:
            temp = carry + l_rem.val
            dsum = temp % 10
            carry = 1 if temp > 9 else 0
            ans.next = ListNode(dsum)
            ans = ans.next
            l_rem = l_rem.next

        if carry:
            ans.next = ListNode(carry)

        return a
















