class Node:
    def __init__(self):
        self.children = [None]*26
        self.end = False


class WordDictionary:

    def __init__(self):
        self.array = Node()

    def addWord(self, word: str) -> None:
        array = self.array
        for w in word:
            i = ord(w) - ord('a')
            if not array.children[i]:
                array.children[i] = Node()
            array = array.children[i]
        array.end = True
        

    def search(self, word: str) -> bool:

        def traverse(word, array):
            for x in range(len(word)):
                w = word[x]
                i = ord(w) - ord('a')
                if w == '.':
                    res = False
                    for j in range(26):
                        if array.children[j] and traverse(word[x+1:], array.children[j]):
                            return True
                    return res
                if not array.children[i]:
                    return False
                
                array = array.children[i]
            return array.end

        return traverse(word, self.array)
        
        
