class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + carry
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                carry = 1
            else:
                carry = 0

        # print(digits, carry)
        if carry == 1:
            # digits[0] %= 10
            ans = [1, *digits]
            return ans
        else:
            return digits
        