class Node:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.next = None


class PrefixTree:

    def __init__(self):
        self.array = [None]*26
        
    def insert(self, word: str) -> None:
        array = self.array
        for x in range(len(word)):
            w = word[x]
            i = ord(w) - ord('a')
            if not array[i]:
                array[i] = Node(w)

            if not array[i].next and x+1 < len(word):
                array[i].next = [None]*26
            
            if x+1 == len(word):
                array[i].end = True

            array = array[i].next


    def search(self, word: str) -> bool:
        array = self.array
        for x in range(len(word)):
            w = word[x]
            i = ord(w) - ord('a')
            if not array:
                return False
            if not array[i]:
                return False
            if not array[i].next and x+1 < len(word):
                return False
            if array[i].end is True and x+1 == len(word):
                return True
            array = array[i].next
        return False
        

    def startsWith(self, prefix: str) -> bool:
        array = self.array
        for x in range(len(prefix)):
            w = prefix[x]
            i = ord(w) - ord('a')
            if not array:
                return False
            if not array[i]:
                return False
            if not array[i].next and x+1 < len(prefix):
                return False
            array = array[i].next
        return True
        
        
        