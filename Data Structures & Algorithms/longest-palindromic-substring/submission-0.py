class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        reslen = 0

        for i in range(len(s)):
            # odd 
            p = q = i
            while p >= 0 and q < len(s):
                if s[p] == s[q]:
                    # print("odd", p,q, res, reslen)
                    if q-p+1 > reslen:
                        # print("bigger₹")
                        res = p
                        reslen = q-p+1
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
                    if q-p+1 > reslen:
                        # print("bigger@")
                        res = p
                        reslen = q-p+1
                    p -= 1
                    q += 1
                else:
                    break

        return s[res: res+reslen]