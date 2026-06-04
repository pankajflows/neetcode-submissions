class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # For each cell
        # Mark it visited if not already done
        # if visited ignore
        # take its left, right, top, bottom element one by one and send it 

        def bfs(i, j, queue):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0" # visited
            # take its left, right, top, bottom element one by one and dd them to queue
            if j-1 >=0 and grid[i][j-1] != "0": # left
                queue.append((i,j-1))
            if j+1 < len(grid[i]) and grid[i][j+1] != "0": # right
                queue.append((i, j+1))
            if i-1 >= 0 and grid[i-1][j] != "0": # top
                queue.append((i-1, j))
            if i+1 < len(grid) and grid[i+1][j] != "0":
                queue.append((i+1, j))

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1
                    new_queue = deque()
                    new_queue.append((i,j))
                    while new_queue:
                        p,q = new_queue.popleft()
                        bfs(p,q, new_queue)

        return ans


