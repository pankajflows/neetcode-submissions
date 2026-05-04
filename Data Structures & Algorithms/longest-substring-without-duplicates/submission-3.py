class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        i = 0
        j = 0
        bank = {}
        ans = 0

        while j < len(s):
            bank[s[j]] = bank.get(s[j], 0) + 1

            while bank[s[j]] > 1:
                bank[s[i]] -= 1
                i += 1
                
            ans = max(ans, j-i+1)
            j += 1

        return ans
