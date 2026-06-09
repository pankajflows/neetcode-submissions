class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self):
                # Initially, every element is its own parent
                self.parent = dict()
                # Initially, every set has a size of 1
                self.size = defaultdict(lambda: 1)

            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                """Finds the representative of the set containing x with path compression."""
                if self.parent[x] != x:
                    # Recursively find the root and compress the path
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                """Merges the sets containing x and y using union by size."""
                root_x = self.find(x)
                root_y = self.find(y)

                # Elements are already in the same set
                if root_x == root_y:
                    return False 

                # Attach the smaller tree to the root of the larger tree
                if self.size[root_x] < self.size[root_y]:
                    self.parent[root_x] = root_y
                    self.size[root_y] += self.size[root_x]
                else:
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]
                    
                return True

        uf = UnionFind()
        ans = list()
        for v1, v2 in edges:
            if not uf.union(v1, v2):
                ans.append([v1, v2])

        return ans[-1]

        







