"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def maker(node, node_bank):
            # print("making", node)
            if not node:
                return
            if node.val not in node_bank:
                node_bank[node.val] = Node(node.val)
            else:
                return node_bank[node.val]
            for neigh in node.neighbors:
                created_neighbor = maker(neigh, node_bank)
                if created_neighbor:
                    node_bank[node.val].neighbors.append(created_neighbor)
            return node_bank[node.val]

        node_bank = dict()
        return maker(node, node_bank)


        