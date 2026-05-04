class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1count = [0]*26
        s2count = [0]*26

        for s in s1:
            s1count[ord(s) - ord('a')] += 1
        for s in s2[:len(s1)]:
            s2count[ord(s) - ord('a')] += 1

        i = 0
        j = len(s1)

        while j < len(s2):
            if s1count == s2count:
                return True

            s2count[ord(s2[i]) - ord('a')] -= 1
            s2count[ord(s2[j]) - ord('a')] += 1

            i += 1
            j += 1

        return s1count == s2count
        