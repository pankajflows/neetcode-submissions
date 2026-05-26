# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [None]
        def traverse(root):
            if not root:
                return 0

            lsum = traverse(root.left)
            rsum = traverse(root.right)

            poss1 = lsum + root.val
            poss2 = rsum + root.val
            poss3 = lsum + rsum + root.val

            maxi1 = max(poss1, poss2, poss3, root.val)
            maxi2 = max(poss1, poss2, root.val)
            # print(poss1, poss2, poss3, maxi1, ans[0])
            ans[0] = max(ans[0], maxi1) if ans[0] else maxi1
            return maxi2

        traverse(root)
        return ans[0]































        