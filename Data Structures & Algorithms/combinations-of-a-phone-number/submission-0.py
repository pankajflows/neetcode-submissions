class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(i, arr):
            if i+1 > len(digits):
                ans.append("".join(arr))
                return
            
            for alphabet in t9[digits[i]]:
                backtracking(i+1, arr+[alphabet])

        ans = list()
        t9 = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        backtracking(0, [])
        return ans if len(digits) > 0 else []
        