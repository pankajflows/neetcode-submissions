# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(node):
            if not node:
                return 0, True
            l, l_decision = balance(node.left)
            r, r_decision = balance(node.right)
            if not l_decision or not r_decision:
                return float("inf"), False

            diff = abs(l-r)
            lr_max = max(l,r)
            return (1+lr_max, True) if diff <= 1 else (1+lr_max, False)


        return balance(root)[1]