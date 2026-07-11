class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import cache

        @cache
        def rec(i,j):
            if j == len(p):
                return i == len(s)

            if i == len(s):
                if j+1 < len(p) and p[j+1] == '*':
                    return rec(i,j+2)
                return False

            if j+1 < len(p) and p[j+1] == '*':
                if rec(i, j+2):
                    return True
                if s[i] == p[j] or p[j] == '.':
                    return rec(i+1,j)
                return False
            else:
                if s[i] == p[j] or p[j] == '.':
                    return rec(i+1, j+1)
                return False

        return rec(0,0)


        