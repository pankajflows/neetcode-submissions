class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([c.lower() if c.isalpha() or c.isdigit() else "" for c in s])
        
        i = 0
        j = len(new_s)-1

        print(new_s)

        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        return True
        