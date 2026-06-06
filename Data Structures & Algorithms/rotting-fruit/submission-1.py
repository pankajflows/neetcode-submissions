class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def spread(i, j, dist):
            # print("spread", i,j)
            if grid[i][j] == 0:
                return -1
            if (i, j) in visited and visited[(i, j)] <= dist:
                return
            visited[(i,j)] = dist
            

            for mi,mj in ((-1,0), (1,0), (0,-1), (0,1)):
                p = i+mi*1
                q = j+mj*1
                # print("makinf", p,q)
                if p >= 0 and p < len(grid) and q >= 0 and q < len(grid[i]):
                    spread(p, q, dist+1)


        mx = 0
        visited = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    spread(i,j,0)
        # print(visited)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if (i,j) not in visited:
                        return -1
                    mx = max(mx, visited[(i,j)])

        return mx