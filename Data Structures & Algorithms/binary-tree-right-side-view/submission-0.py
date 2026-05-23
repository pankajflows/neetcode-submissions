# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = list()
        queue = deque()
        queue.append(root)

        while queue:
            level_nodes = list()
            while queue:
                level_nodes.append(queue.popleft())
            for i in range(len(level_nodes)):
                curr = level_nodes[i]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if i == len(level_nodes)-1:
                    ans.append(level_nodes[-1].val)

        return ans
        