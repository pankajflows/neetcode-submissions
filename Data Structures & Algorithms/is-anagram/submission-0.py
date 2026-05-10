class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = [0]*26
        ta = [0]*26

        for a in s:
            i = ord(a) - ord('a')
            sa[i] += 1
        for a in t:
            i = ord(a) - ord('a')
            ta[i] += 1

        return sa == ta
             