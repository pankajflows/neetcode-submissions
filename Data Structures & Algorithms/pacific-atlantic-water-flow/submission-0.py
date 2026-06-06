class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        preach = set()
        areach = set()
        # preach = [[False for i in range(len(heights[0]))]]*len(heights)
        # areach = [[False for i in range(len(heights[0]))]]*len(heights)

        def dfs(i, j, prev_height, set_):
            # print(i,j)
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i,j) in set_:
                return
            elif heights[i][j] >= prev_height:
                set_.add((i,j))
                for mi,mj in ((-1,0), (1,0), (0,-1), (0,1)):
                    dfs(i+1*mi, j+1*mj, heights[i][j], set_)

        # for each pacific touching cell
        # dfs and see how far is reachable
        for i in range(len(heights[0])):
            dfs(0,i,0, preach)
            dfs(len(heights)-1, i, 0, areach)
        for i in range(len(heights)):
            dfs(i,0,0, preach)
            dfs(i, len(heights[0])-1, 0, areach)
        # for each atlantic touching cell
        # dfs and see how far is reachable

        # check both matrixes, if both are reachable then include in your ans
        ans = list()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in preach and (i,j) in areach:
                    ans.append([i,j])

        return ans
         
        