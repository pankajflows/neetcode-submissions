class Solution:
    def getSum22(self, a: int, b: int) -> int:
        carries = [0] * 32
        ans = 0

        for i in range(32):
            if (a&(1<<i)) or (b&(1<<i)) or carries[-i]:
                carries[-i-1] = 1
                ans |= (1<<i)
        return ans


    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for pos in range(32):
            bit1 = (a >> pos) & 1
            bit2 = (b >> pos) & 1
            current_carry = carry
            
            current_res = bit1 ^ bit2 ^ current_carry
            carry = (bit1 & bit2) | (current_carry & (bit1 ^ bit2))

            res = res | (current_res << pos)

        if res >= 2**31:
            res = res - 2**32

        return res




            





