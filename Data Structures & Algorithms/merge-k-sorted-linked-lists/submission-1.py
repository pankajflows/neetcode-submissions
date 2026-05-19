# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(l1, l2):
            l3 = curr = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
                
            return l3.next

        def mergeSort(alist):
            if len(alist) <= 1:
                return alist[0]

            mid = len(alist) // 2
            left_list = alist[:mid]
            right_list = alist[mid:]

            sorted_left = mergeSort(left_list)
            sorted_right = mergeSort(right_list)

            return mergeTwoLists(sorted_left, sorted_right)


        return mergeSort(lists)        





















