class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # row swapping
        p, q = 0, len(matrix)-1

        while p < q:
            for j in range(len(matrix[0])):
                print(p,j, q)
                temp = matrix[p][j]
                matrix[p][j] = matrix[q][j]
                matrix[q][j] = temp

            p += 1
            q -= 1


        # transpose a matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        

        