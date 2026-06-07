class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = list()
        indegree = {i:0 for i in range(numCourses)}
        neighbours = {k: set() for k in indegree.keys()}

        for p,q in prerequisites:
            indegree[p] += 1
            neighbours[q].add(p)

        queue = deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)

        # print("quue before", queue)
        # print("indegree", indegree)
        # print("neighbours", neighbours)
        count = 0
        while queue:
            c = queue.popleft()
            ans.append(c)
            count += 1
            for n in neighbours[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

        # print(ans)
        # print(indegree, count)
        for k,v in indegree.items(): 
            if v < 0:
                return []
        return ans if len(ans) == numCourses else []

        