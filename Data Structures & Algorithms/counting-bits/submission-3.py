class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        bank = [None]*(n+n)
        # print(bank)
        bank[0] = 0
        bank[1] = 1
        ans = list()
        factor = 4

        for i in range(n+1):
            if i < 2:
                ans.append(bank[i])
            elif i < factor:
                a = bank[i-(factor//2)] + 1
                bank[i] = a
                ans.append(a)
            if i == factor-1:
                factor *= 2

        return ans 

        