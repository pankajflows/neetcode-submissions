class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from functools import reduce
        longest_word_len = reduce(lambda x,y: max(x, len(y)), words, 0)
        indegree = {w: 0 for word in words for w in word}
        adj_list = defaultdict(set)

        # making the indegree dict
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minlen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""

            for j in range(minlen):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        # adding zero indegrees alphabest to queue
        queue = deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)
        
        # exploring the queue and its neighbours
        ans = list()
        while queue:
            a = queue.popleft()
            ans.append(a)

            for neighbour in adj_list[a]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(indegree) != len(ans):
            return ""
        
        return ''.join(ans)