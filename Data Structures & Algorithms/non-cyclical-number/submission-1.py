class Solution:
    def isHappy(self, n: int) -> bool:
        # print(n)
        if n==4:
            return False
        if n==1:
            return True
        return self.isHappy(sum([int(ni)*int(ni) for ni in str(n)]))
        