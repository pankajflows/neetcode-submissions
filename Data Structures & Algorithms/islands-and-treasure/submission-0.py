class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def spread(i, j, dist):
            # print(i,j)
            if grid[i][j] == -1:
                return

            if grid[i][j] == float("inf"):
                grid[i][j] = dist
            elif grid[i][j] < float("inf") and grid[i][j] > 0:
                grid[i][j] = min(grid[i][j], dist)
                if grid[i][j] < dist:
                    return

            for mi,mj in ((-1,0), (1,0), (0,-1), (0,1)):
                p = i+mi*1
                q = j+mj*1
                if p >= 0 and p < len(grid) and q >= 0 and q < len(grid[i]):
                    spread(p, q, dist+1)
            




        # visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    spread(i,j,0)



        

        