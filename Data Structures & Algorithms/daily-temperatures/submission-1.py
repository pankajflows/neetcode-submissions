class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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
        