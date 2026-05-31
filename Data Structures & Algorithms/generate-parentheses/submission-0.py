class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op, cl, arr):
            # if cl > op or op > n or cl > n:
            #     return
            if len(arr) == 2*n:
                ans.append(''.join(arr))
                return

            if op < n:
                arr.append('(')
                backtrack(op+1, cl, arr)
                arr.pop()

            if cl < n and cl < op:
                arr.append(')')
                backtrack(op, cl+1, arr)
                arr.pop()
            
            

        ans = list()
        backtrack(0, 0, [])
        return ans
