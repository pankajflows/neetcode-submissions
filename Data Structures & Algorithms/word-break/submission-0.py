class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import cache
        @cache
        def rec(i,j):
            # print(i,j)
            if j > len(s)-1:
                return
            if j == len(s)-1 and s[i:j+1] in bank:
                print('jackpot')
                ans[0] = True

            if j < len(s) and s[i:j+1] in bank:
                # do I start looking for next word
                rec(j+1, j+1)

            # do I keep expanding on the current word
            rec(i, j+1)

        bank = set(wordDict)
        ans = [False]
        rec(0,0)
        return ans[0]

    