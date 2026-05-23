# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        else:
            return []
        ans = list()
        tans = list()
        print(queue)

        while queue:
            level_nodes = list()
            tans = list()
            while queue:
                level_nodes.append(queue.popleft())
            for node in level_nodes:
                tans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(tans)
        return ans

        