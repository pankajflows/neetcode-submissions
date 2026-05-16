class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    def minWindow2(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        if len(t) > len(s):
            return ""
        # make set of t
        from collections import Counter
        t_counter = Counter(t)
        print(t_counter)

        # loop over s from both ends and keep shortening the window
        # each time check whether we have everthing from t or not
        # prioritize moving from left, if not at all possible move from right

        def membership(substr, countersent):
            substr = Counter(substr)
            return substr >= countersent

        substr_candidates = dict()
        bleft = 0
        bright = len(s)-1
        bdiff = float("inf")

        for i in range(len(s)):
            for j in range(i, len(s)):
                if membership(s[i:j+1], t_counter) and j-i< bdiff:
                    bright = j
                    bleft = i
                    bdiff = j-i
                    print(bleft, bright)
                

        return s[bleft: bright+1]


        # while i <= j:
        #     print("aai", i, "jay", j)
        #     if membership(s[i:j+1], t_counter):
        #         print("membership pass", i, j)
        #         substr_candidates[i] = j
        #         if leftexhausted:
        #             j -= 1
        #         else:
        #             i += 1
        #     else:
        #         print("failed membership", i, j)
        #         if leftexhausted and rightexhausted:
        #             print("exjhausted here", i, j)
        #             break
        #         elif leftexhausted:
        #             rightexhausted = True
        #         leftexhausted = True
        #         i -= 1

        # print(substr_candidates)

        # ans_size = float("infinity")
        # ans = ""
        # for k,v in substr_candidates.items():
        #     if v-k < ans_size:
        #         ans_size = v-k
        #         ans = s[k:v+1]

        # print(ans, ans_size)
        # return ans
        


        




        # return ""