class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import cache

        @cache
        def rec(i,j):
            if i >= len(word1):
                return len(word2)-j
            if j >= len(word2):
                return len(word1)-i

            a = b = c = float("inf")
            if word1[i] == word2[j]:
                a = rec(i+1, j+1)
            
            # insert
            b = 1 + rec(i, j+1)

            # delete
            c = 1 + rec(i+1, j)

            # replace
            d = 1 + rec(i+1, j+1)

            return min(a,b,c, d)

        return rec(0,0)

            
        