class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1]*n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return False

                if self.size[root_x] < self.size[root_y]:
                    self.parent[root_x] = root_y
                    self.size[root_y] += self.size[root_x]
                else:
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]

                return True

        uf = UnionFind(n)
        res = n
        for v1, v2 in edges:
            if uf.union(v1, v2):
                res -= 1

        return res
         