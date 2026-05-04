class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        freq = dict()

        for r in range(len(s)):
            c = s[r]
            
            freq[c] = freq.get(c, 0) + 1

            length = r - l + 1

            if length - max(freq.values()) <= k:
                ans = max(ans, length)
            else:
                freq[s[l]] -= 1
                l += 1

        return ans
        