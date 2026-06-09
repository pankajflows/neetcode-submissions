class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wild_bank = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                wilded = word[:i] + '*' + word[i + 1:]
                wild_bank[wilded].add(word)

        queue = deque()
        visited = set(beginWord)
        queue.append((beginWord, 1))

        while queue:
            w, l = queue.popleft()
            if w == endWord:
                return l
            for i in range(len(w)):
                wilded = w[:i] + '*' + w[i + 1:]
                if wilded in wild_bank:
                    for candidate in wild_bank[wilded]:
                        if candidate not in visited:
                            queue.append((candidate, l+1))
                            visited.add(candidate)

        return 0



