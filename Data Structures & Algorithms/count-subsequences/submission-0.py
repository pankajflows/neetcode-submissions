class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        from functools import cache

        @cache
        def rec(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0

            a = b = 0
            if s[i] == t[j]:
                a = rec(i+1, j+1)
            b = rec(i+1, j)

            return a+b


        return rec(0, 0)
