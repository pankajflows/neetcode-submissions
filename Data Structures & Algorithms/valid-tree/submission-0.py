class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # detech loop
        # detech disconnection

        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        print(adj)

        def dfs(e, parent, visited):
            if e is None:
                return True
            if e in visited:
                return False
            visited.add(e)

            for ele in adj[e]:
                if ele == parent:
                    continue
                if not dfs(ele, e, visited):
                    return False
            return True

        v = set()
        dfs_report = dfs(0, -1, v)
        print(v)
        if len(v) == n:
            return dfs_report
        else:
            return False
            
        
        
        