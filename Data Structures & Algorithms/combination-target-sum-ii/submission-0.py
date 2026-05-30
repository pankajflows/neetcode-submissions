class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(i, arr, result):
            # print(i, arr, result)
            if result == 0:
                ans.append(arr.copy())
                return
            elif result < 0 or i > len(candidates)-1:
                return

            arr.append(candidates[i])
            backtracking(i+1, arr, result-candidates[i])
            arr.pop()

            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            backtracking(j, arr, result)

        candidates.sort()
        ans = list()
        backtracking(0, [], target)
        return ans

        