class Solution:
    def partitionLabels22(self, s: str) -> List[int]:
        bank = dict()
        ans = list()
        for i in range(len(s)):
            if s[i] not in bank:
                bank[s[i]] = [i,None]
            else:
                bank[s[i]][1] = i

        i = 0
        j = 0

        while i < len(s):
            if bank[s[i]][1]:
                j = bank[s[i]][1]
                print("running in", list(range(i+1, bank[s[i]][1])))
                for k in range(i+1, bank[s[i]][1]):
                    if not bank[s[k]][1]:
                        continue
                    j = max(j, bank[s[k]][1])

                ans.append(j-i+1)
                i = j+1
                k = i
            else:
                ans.append(1)
                i += 1
                j += 1

        return ans


    def partitionLabels(self, s: str) -> List[int]:
        bank = dict()
        ans = list()
        for i in range(len(s)):
            if s[i] not in bank:
                bank[s[i]] = [i,None]
            else:
                bank[s[i]][1] = i

        i = 0
        j = 0
        k = 0

        while i < len(s):
            if bank[s[k]][1]:
                j = max(j, bank[s[k]][1])

            k += 1
            if k >= j:
                ans.append(j-i+1)
                i = j+1
                j = i
                k = i
        

        return ans

        