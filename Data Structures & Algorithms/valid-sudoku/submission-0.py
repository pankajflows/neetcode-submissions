class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        hashsetrow = [set() for i in range(9)]
        hashsetcol = [set() for i in range(9)]
        hashsetintbox = [[set() for i in range(3)] for j in range(3)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    ele = int(board[i][j])
                    if ele in hashsetrow[i] or ele in hashsetcol[j] or ele in hashsetintbox[i//3][j//3]:
                        return False
                    hashsetrow[i].add(ele)
                    hashsetcol[j].add(ele)
                    hashsetintbox[i//3][j//3].add(ele)

        
        return True