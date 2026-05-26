# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = list()
        def traverse(node):
            if not node:
                return "#"
            ans.append(str(node.val))

            n = traverse(node.left)
            # print("from left", n)
            if n:
                ans.append(n)

            n = traverse(node.right)
            # print("from right", n)
            if n:
                ans.append(n)

        traverse(root)
        # print(ans)
        return " ".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        de_ans = data.split(" ")
        def traverse():
            d = next(items)
            if not d or d == "#":
                return None
            node = TreeNode(d)
            node.left = traverse()
            node.right = traverse()
            return node


        items = iter(de_ans)
        return traverse()
