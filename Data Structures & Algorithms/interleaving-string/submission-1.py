class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        from functools import cache

        @cache
        def rec(i,j):
            if i >= len(s1) and j >= len(s2):
                return True

            k = i+j

            # if k >= len(s3):
            #     return True

            a = b = False
            if i < len(s1) and s3[k] == s1[i]:
                a = rec(i+1, j)
                
            if j < len(s2) and s3[k] == s2[j]:
                b = rec(i, j+1)
            return a or b

        return rec(0,0)
        
        