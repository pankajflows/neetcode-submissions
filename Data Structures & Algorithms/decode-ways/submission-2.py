class Solution:
    def numDecodings2(self, s: str) -> int:
        if s[0] == "0":
            return 0
        bank = {str(i+1): chr(ord('A')+i) for i in range(26)}

        def recurse(i,k):
            if i+k > len(s)-1:
                return

            if s[i:i+k] in bank:
                ans[0] += 1
                recurse(i,k+1)
            else:
                recurse(i+1,0)

        
        ans = [0]
        recurse(0,0)
        return ans[0]
    

    def numDecodings(self, s: str) -> int:
        if s and s[0] == "0":
            return 0
        bank = {str(i) for i in range(1,27)}

        from functools import cache
        @cache
        def rec(i):
            if i >= len(s):
                return 1
            elif s[i] == "0":
                return 0

            f = g = 0
            if i < len(s) and s[i] in bank:
                f = rec(i+1)
            if i+1 < len(s) and s[i:i+2] in bank:
                g = rec(i+2)

            return f+g


        return rec(0)


