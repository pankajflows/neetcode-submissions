class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        operators = {'+', '-', '*', '/'}
        stack = deque()

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                op = t

                if op == "+":
                    op3 = op2 + op1
                elif op == "-":
                    op3 = op2 - op1
                elif op == "*":
                    op3 = op2 * op1
                elif op == "/":
                    op3 = int(op2 / op1)

                stack.append(op3)
        print(stack)
        return stack.pop()
