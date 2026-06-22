class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        def sum_strings(str1, str2):
            return int(str1) + int(str2)

        if len(num1) < len(num2):
            temp = num1
            num1 = num2
            num2 = temp

        p = 0
        rows = list()
        for j in range(len(num2)-1, -1, -1):
            carry = 0
            row = list()
            for i in range(len(num1)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                mul += carry
                carry = mul // 10
                mul = mul % 10
                row.append(str(mul))
            if carry > 0:
                row.append(str(carry))

            pad = list()
            for k in range(p):
                pad.append('0')
            p += 1

            row = "".join(reversed(row)) + "".join(pad)
            rows.append(row)

        ans = 0
        for row in rows:
            ans += int(row)

        return str(ans)
            



        