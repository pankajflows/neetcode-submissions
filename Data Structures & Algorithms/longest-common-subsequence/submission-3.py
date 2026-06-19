class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import cache
        @cache
        def rec(i, j):
            a = b = c = 0
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                b = 1 + rec(i+1, j+1)
            else:
                a += rec(i+1, j)
                c += rec(i, j+1)

            return max(a,b,c)

        return rec(0,0)