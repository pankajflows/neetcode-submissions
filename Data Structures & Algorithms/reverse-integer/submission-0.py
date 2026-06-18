class Solution:
    def reverse(self, x: int) -> int:
        ans = 0

        mx = 2147483647
        mi = -2147483648

        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if ans > mx//10 or (ans == mx//10 and digit >= mx%10):
                return 0
            elif ans < mi/10 or (ans == mi//10 and digit <= mx%10):
                return 0


            ans = (ans*10)+digit
            # if ans > mx or ans < mi:
            #     return 0

        return ans
            