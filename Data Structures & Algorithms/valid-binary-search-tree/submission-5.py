# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, ll, rl):
            if node is None:
                return True
            if not (ll < node.val < rl):
                return False
            if node.left and (node.left.val >= node.val or node.left.val < ll):
                # print("rpeorting falsel", node.val)
                return False
            if node.right and (node.right.val <= node.val or node.right.val > rl):
                # print("rpeorting falser", node.val)
                return False

            # print("before return", node.val, ll, rl)
            return dfs(node.left, ll, node.val) and dfs(node.right, node.val, rl)

        return dfs(root, -float("inf"), float("inf"))

        