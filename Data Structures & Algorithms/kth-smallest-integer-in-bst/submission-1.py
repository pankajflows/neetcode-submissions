# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]

        def dfs(node):
            if not node:
                return
            
            ans = dfs(node.left)
            if ans:
                return ans

            count[0] -= 1
            if count[0] <= 0:
                return node.val
            
            ans = dfs(node.right)
            if ans:
                return ans
        return dfs(root)
            
            
                
            


        