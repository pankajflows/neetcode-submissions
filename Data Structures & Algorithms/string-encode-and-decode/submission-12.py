class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        # ans = ""
        # for s in strs:
        #     ans += s
        #     ans += "\n"

        ans = "\n"
        ans += "\n".join(strs)

        # if len(ans) == 0:
        #     return "\n"
        # else:
        #     return ans
        return ans

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ans = s.split("\n")

        if len(ans) == 1:
            return []
        else:
            return ans[1:]
