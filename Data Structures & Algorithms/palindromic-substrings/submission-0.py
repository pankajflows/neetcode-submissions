class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        reslen = 0
        count = 0

        for i in range(len(s)):
            # odd 
            p = q = i
            while p >= 0 and q < len(s):
                if s[p] == s[q]:
                    count += 1
                    p -= 1
                    q += 1
                else:
                    break

            # even
            p = i
            q = i+1
            while p >= 0 and q < len(s):
                if s[p] == s[q]:
                    # print("even", p,q, res, reslen, p-q+1)
                    count += 1
                    p -= 1
                    q += 1
                else:
                    break

        return count