class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = list()

        while matrix:
            top_row = matrix[0]
            for t in top_row:
                ans.append(t)

            matrix.pop(0)
            # print("before", matrix)
            matrix = [list(row) for row in reversed(list(zip(*matrix)))]
            # print("after", matrix)

        return ans
        