class Solution:
    def solveNQueens2(self, n: int) -> List[List[str]]:
        # simple approach with manual O(n) check
        def check(row, col, board):
            # print("check", row, col, board)
            for i in range(row): # any prev queens in same col ?
                if board[i][col] == 'Q':
                    return False

            i = row-1
            j = col-1
            p = row-1
            q = col+1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            while p>=0 and q<n:
                if board[p][q] == 'Q':
                    return False
                p -= 1
                q += 1
            # print("True")
            return True


        board = [['.' for i in range(n)] for j in range(n)]

        def magic(row, board):
            if row == n:
                # print(board)
                ans.append([''.join(row) for row in board])
                return

            for i in range(n):
                # print(row, i)
                board[row][i] = 'Q'
                if check(row, i, board): # checks if the current places queen is safe from previous queens
                    magic(row+1, board)
                board[row][i] = '.'


        ans = list()
        magic(0, board)
        return ans
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        # optimized set based checking
        board = [['.' for i in range(n)] for j in range(n)]
        cc = col_check = set()
        pdc = prev_diagonal_check = set()
        ndc = next_diagonal_check = set()

        def magic(row, board):
            if row == n:
                # print(board)
                ans.append([''.join(row) for row in board])
                return

            for i in range(n):
                if i in cc or row-i in pdc or row+i in ndc: # checks if the current places queen is safe from previous queens
                    continue


                board[row][i] = 'Q'
                cc.add(i)
                pdc.add(row-i)
                ndc.add(row+i)

                magic(row+1, board)

                board[row][i] = '.'
                cc.remove(i)
                pdc.remove(row-i)
                ndc.remove(row+i)


        ans = list()
        magic(0, board)
        return ans


