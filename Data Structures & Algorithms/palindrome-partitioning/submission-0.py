class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(st):
            # checks pallindrome
            if len(st) == 0:
                return False
            i = 0
            j = len(st)-1
            while i < j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            return True


        def backtracking(start, arr):
            if start == len(s):
                ans.append(arr.copy())
                return

            for end in range(start+1, len(s)+1):
                a = s[start:end]
  
                if check(a):
                    arr.append(a)
                    backtracking(end, arr)
                    arr.pop()
        ans = list()
        backtracking(0, [])
        return ans
        