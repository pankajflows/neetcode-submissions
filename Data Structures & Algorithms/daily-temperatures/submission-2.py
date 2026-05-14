class Solution:
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        mstack = collections.deque()
        ans = [0]*len(temperatures)

        for k in range(len(temperatures)-1, -1, -1):
            v = temperatures[k]
            while mstack and temperatures[mstack[-1]] <= v:
                mstack.pop()
            if mstack:
                ans[k] = mstack[-1]-k
            mstack.append(k)

        # print(mstack)
        return ans
        
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = deque()
        ans = [-1]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            v = temperatures[i]

            while len(monostack) > 0 and v >= monostack[-1][1]:
                monostack.pop()

            if len(monostack) <= 0:
                ans[i] = 0
            else:
                d = monostack[-1][0] - i
                ans[i] = d

            monostack.append((i, v))

        return ans








