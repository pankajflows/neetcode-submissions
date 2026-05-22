# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dia(node):
            if not node:
                return 0
            l = dia(node.left)
            r = dia(node.right)
            if node.val == 2:
                print(l,r)
            self.ans = max(self.ans, l+r)
            return 1+max(l,r)
        dia(root)
        return self.ans
        