class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def mark(i,j):
            # left
            p,q = i,j
            while q >= 0:
                if matrix[p][q] != 0:
                    matrix[p][q] = None
                q -= 1

            # right
            p,q = i,j
            while q < len(matrix[p]):
                if matrix[p][q] != 0:
                    matrix[p][q] = None
                q += 1

            # top
            p,q = i,j
            while p >= 0:
                if matrix[p][q] != 0:
                    matrix[p][q] = None
                p -= 1

            # bottom
            p,q = i,j
            while p < len(matrix):
                if matrix[p][q] != 0:
                    matrix[p][q] = None
                p += 1

        # mark
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark(i,j)

        
        # sweep
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

        
        