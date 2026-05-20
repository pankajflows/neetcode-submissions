# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Used long making of (start, end) tuples and then joining them. big chances of error
        def reverse_ll(start_node, end_node):
            prev = None
            curr = start_node
            limit = end_node.next
            while curr and curr != limit:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            
            return prev, start_node

        pointer = head
        count = 0
        start = head
        reversed_pairs = list()
        while pointer:
            if count == 0:
                start = pointer
            count += 1
            if count == k:
                print("hit k", start.val, pointer.val)
                local_end = pointer
                new_reversed = reverse_ll(start, local_end)
                reversed_pairs.append(new_reversed)
                count = 0
            pointer = pointer.next

        if count > 0:
            reversed_pairs.append((start, None))

        [print(r[0].val, "-", r[1].val if r[1] else "",  end=", ") for r in reversed_pairs]

        pointer = None
        for i in range(len(reversed_pairs)):
            if i+1 < len(reversed_pairs):
                x = reversed_pairs[i]
                y = reversed_pairs[i+1]
                if not pointer:
                    pointer = x[0]

                x[1].next = y[0]

            else:
                # just join the last
                pointer.next = reversed_pairs[i][0]

        return pointer


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        count = 0
        while node:
            count += 1
            node = node.next

        iters = count // k

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = endnode = head

        for i in range(iters):
            for _ in range(k):
                endnode = endnode.next

            while curr.next != endnode:
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp

            prev = curr
            curr = curr.next

        return dummy.next

                












