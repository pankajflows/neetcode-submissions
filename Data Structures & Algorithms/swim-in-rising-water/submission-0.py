class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # adding first neighbours to heap

        # a = max(grid[0][1], grid[0][0])
        # b = max(grid[1][0], grid[0][0])
        heap = [(grid[0][0], 0, 0)] # (height,x,y))
        n = len(grid)
        x = y = 0
        ans = 0
        visited = set()

        while heap:
            cell = heapq.heappop(heap)
            h, x, y = cell
            if (x,y) in visited:
                continue
            if x == n-1 and y == n-1:
                return h
            ans = max(ans, h)
            visited.add((x,y))
            
            coordinates = ((0,1), (1,0), (0,-1), (-1,0))
            for mulx, muly in coordinates:
                xx = x+mulx
                yy = y+muly
                if xx < 0 or yy < 0 or xx > n-1 or yy > n-1 or (xx, yy) in visited:
                    continue
                hh = max(h, grid[xx][yy])
                heapq.heappush(heap, (hh, xx, yy))

        return -1


            




        