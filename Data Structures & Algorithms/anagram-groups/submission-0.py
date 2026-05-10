class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_bank = collections.defaultdict(list)
        ans = list()
        for i in range(len(strs)):
            astr = strs[i]
            counter = [0]*26
            for a in astr:
                counter[ord(a) - ord('a')] += 1
            counter = tuple(counter)

            counter_bank[counter].append(i)

        for v in counter_bank.values():
            ans.append([strs[index] for index in v])

        return ans


