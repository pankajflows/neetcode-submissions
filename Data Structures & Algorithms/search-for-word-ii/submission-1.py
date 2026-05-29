class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def check_string(self, text: str) -> tuple[bool, bool]:
        """
        Traverses the trie for the given text.
        Returns: (is_exact_word, is_prefix)
        """
        node = self.root
        for char in text:
            if char not in node.children:
                # Character missing means it is neither a word nor a prefix
                return False, False
            node = node.children[char]
        
        # Exact word match depends on the flag
        is_exact_word = node.is_end_of_word
        
        # If the text exists in the trie, it is always a prefix 
        # (even if it only prefixes itself)
        is_prefix = True 
        
        return is_prefix, is_exact_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def check(preformed):
            return bank.check_string(preformed)

        def dfs(i, j, visited, pre):
            if i>=len(board) or i<0 or j<0 or j>=len(board[0]) or (i,j) in visited:
                return False

            preformed = pre + board[i][j]
            prefix_check, word_check = check(preformed)
            if not prefix_check:
                return False
            if word_check:
                ans.add(preformed)
            # print("prefix pass", board[i][j])

            visited.add((i,j))
            top = dfs(i-1,j, visited, preformed)
            down = dfs(i+1,j, visited, preformed)
            left = dfs(i,j-1, visited, preformed)
            right = dfs(i,j+1, visited, preformed)
            visited.remove((i,j))
            # return top or down or left or right

        # loading trie with all words    
        bank = Trie()
        for word in words:
            bank.insert(word)

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                result = dfs(i, j, visited, "")
                # if result is not False:
                #     ans.append(result)

        return list(ans)
        





























