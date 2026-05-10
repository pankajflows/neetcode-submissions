class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append(str(len(s)))
            ans.append("#")
            ans.append(s)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = list()
        i = 0
        print(s)
        l = ""
        while i < len(s):
            ch = s[i]
            if ch == '#':
                print(i,l)
                l = int(l)
                ans.append(s[i+1: i+1+l] or "")
                i = i+1+l
                l = ""
            else:
                l += ch
                i+=1
        return ans