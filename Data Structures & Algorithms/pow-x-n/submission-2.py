class Solution:
    def myPow2(self, x: float, n: int) -> float:
        # brute force
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


    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            if n == 0:
                return 1

            half = rec(x, n//2)
            if n%2 == 0:
                return half*half
            else:
                return half*half*x

        if n < 0:
            ans = rec(x, abs(n))
            return 1/ans
        else:
            return rec(x,n)
        