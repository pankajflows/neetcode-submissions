class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j, queue):
            if grid[i][j] == 0:
                return
            grid[i][j] = 0 # visited
            # take its left, right, top, bottom element one by one and dd them to queue
            if j-1 >=0 and grid[i][j-1] != 0: # left
                queue.append((i,j-1))
            if j+1 < len(grid[i]) and grid[i][j+1] != 0: # right
                queue.append((i, j+1))
            if i-1 >= 0 and grid[i-1][j] != 0: # top
                queue.append((i-1, j))
            if i+1 < len(grid) and grid[i+1][j] != 0:
                queue.append((i+1, j))

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # print(i,j)
                    local_ans = 0
                    new_queue = deque()
                    visited = set()
                    new_queue.append((i,j))
                    while new_queue:
                        p,q = new_queue.popleft()
                        bfs(p,q, new_queue)
                        print("popped", p, q)
                        if (p,q) not in visited:
                            local_ans += 1
                            visited.add((p,q))
                        # print(p,q)
                    ans = max(local_ans, ans)

        return ans