# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        bank = dict()
        for i in range(len(inorder)):
            bank[inorder[i]] = i

        def helper(preorder, inorder, bank):
            if not preorder:
                return None

            root = TreeNode(preorder[0])
            index = bank[preorder[0]] - bank[inorder[0]]

            root.left = helper(
                preorder[1:index+1],
                inorder[:index],
                bank
            )
            root.right = helper(
                preorder[index+1:],
                inorder[index+1:],
                bank
            )
            return root

        return helper(preorder, inorder, bank)