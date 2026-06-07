class Solution:
    def solve2(self, board: List[List[str]]) -> None:

        def dfs(i, j, capture):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i,j) in visited or board[i][j] != "O":
                return True
            # print(i,j, capture)
            if board[i][j] == "O":
                visited.add((i,j))
                if i==0 or i == len(board)-1 or j==0 or j==len(board[0])-1:
                    print("making capture falswe")
                    capture = False
                for mi,mj in ((-1,0), (1,0), (0,-1), (0,1)):
                    capture &= dfs(i+1*mi, j+1*mj, capture)

            if capture:
                board[i][j] = "X"

            return capture


        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i, j, True)


    def solve(self, board: List[List[str]]) -> None:
        # mark safe and then capture
        def dfs_safe(i, j, visited):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i,j) in visited or board[i][j] in "XS":
                return
            visited.add((i,j))
            board[i][j] = "S"
            for mi,mj in ((-1,0), (1,0), (0,-1), (0,1)):
                dfs_safe(i+mi, j+mj, visited)

        # marking safes
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0 or i == len(board)-1 or j==0 or j==len(board[0])-1:
                    dfs_safe(i,j, visited)

        # capturing by sweep and reverting S markers
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"



