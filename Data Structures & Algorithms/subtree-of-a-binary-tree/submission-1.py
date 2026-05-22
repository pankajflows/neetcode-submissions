# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subroot_check(a,b):
            if not a and b:
                return False
            elif a and not b:
                return False
            elif not a and not b:
                return True

            if a.val != b.val:
                return False
            l = subroot_check(a.left, b.left)
            r = subroot_check(a.right, b.right)
            return l and r

        def find_starting(node, sub_node):
            if not node:
                return
            curr_result = False
            if node.val == sub_node.val:
                print("checking", node.val, sub_node.val)
                print("check ans", subroot_check(node, sub_node))
                curr_result = subroot_check(node, sub_node)

            l_result = find_starting(node.left, sub_node)
            r_result = find_starting(node.right, sub_node)
            return l_result or r_result or curr_result

        return True if find_starting(root, subRoot) is True else False

