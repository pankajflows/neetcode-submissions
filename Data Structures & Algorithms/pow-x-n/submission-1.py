class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            limit = abs(n)
            ans = x
            for i in range(1,limit):
                ans *= x
                print(ans)
            ans = 1 / ans
        else:
            limit = n
            ans = x
            for i in range(1, limit):
                ans *= x
        
        return ans


        