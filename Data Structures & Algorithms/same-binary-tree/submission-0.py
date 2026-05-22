# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(a,b):
            if not a and b:
                return False
            elif a and not b:
                return False
            elif not a and not b:
                return True

            if a.val != b.val:
                return False
            l = traverse(a.left, b.left)
            r = traverse(a.right, b.right)
            return l and r

        return traverse(p,q)
        