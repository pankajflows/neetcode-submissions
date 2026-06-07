class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's Algorithm

        if len(prerequisites) == 0:
            return True
        # Calculate indegree of all nodes
        indegree = defaultdict(int)
        neighbors = defaultdict(set)
        for s, p in prerequisites:
            indegree[s] += 1
            neighbors[p].add(s)

        # capturing all top subjects
        for s, p in prerequisites:
            if p not in indegree:
                indegree[p] = 0

        # Add all subjects having zero requisites in queue (indegree = 0)
        queue = deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)

        # Take items from queue and compelete it,
        # Repeatedly pop from the queue, “take” that course, 
        # and decrement in-degrees of its neighbors
        taken = set()
        while queue:
            done = queue.popleft()
            if done in taken:
                return False
            else:
                taken.add(done)
            done_neighbors = neighbors[done]
            # print("done neighbors", done_neighbors)
            for done_neighbor in done_neighbors:
                indegree[done_neighbor] -= 1
                # print(indegree)
                # whenever a neighbor’s in-degree becomes 0, push it to the queue
                if indegree[done_neighbor] == 0:
                    queue.append(done_neighbor)

        print(taken)
        return len(taken) == len(indegree)

        