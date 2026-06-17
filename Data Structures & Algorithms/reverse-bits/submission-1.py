class Solution:
    def reverseBits(self, n: int) -> int:

        # checking fartherst set bit
        ans = 0
        for i in range(32):
            if n & (1 << i):
                ans |= (1 << 31-i)

        return ans