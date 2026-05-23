# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def good(node, umax):
            if not node:
                return
            if node.val >= umax:
                umax = node.val
                # print("umax", umax)
                count[0] += 1
            
            good(node.left, umax)
            good(node.right, umax)

        good(root, root.val-1)
        return count[0]
                
        