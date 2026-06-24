class Solution:
    def checkValidString(self, s: str) -> bool:
        par = deque()
        star = deque()

        for i in range(len(s)):
            a = s[i]
            if a == '(':
                par.append(i)
            elif a == ')':
                if len(par) <= 0:
                    if len(star) > 0:
                        star.pop()
                    else:
                        return False
                else:
                    par.pop()
            elif a == '*':
                star.append(i)
            # else:
            #     return False

        if len(par) == 0:
            return True

        while par:
            if len(star) == 0:
                return False
            elif par[-1] < star[-1]:
                par.pop()
                star.pop()
            else:
                return False

        return True
        