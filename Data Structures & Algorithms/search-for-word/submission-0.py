class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(k, i, j):
            prefix_check = False
            word_check = False

            if board[i][j] == word[k]:
                prefix_check = True
            if prefix_check and len(word)-1 == k:
                word_check = True

            return prefix_check, word_check

        def dfs(i, j, visited, k):
            if i>=len(board) or i<0 or j<0 or j>=len(board[0]) or (i,j) in visited:
                return False
            
            # print("visiting", board[i][j], (i,j), k)

            prefix_check, word_check = check(k, i, j)
            if not prefix_check:
                return False
            if word_check:
                return True
            # print("prefix pass", board[i][j])

            visited.add((i,j))
            top = dfs(i-1,j, visited, k+1)
            down = dfs(i+1,j, visited, k+1)
            left = dfs(i,j-1, visited, k+1)
            right = dfs(i,j+1, visited, k+1)
            visited.remove((i,j))
            return top or down or left or right
            

        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                k = 0
                if dfs(i, j, visited, k):
                    return True

        return False
        
        