class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            if token == '+':
                if stack:
                    val = stack.pop() + stack.pop()
                    stack.append(val)
            if token == "*":
                if stack:
                    val = stack.pop() * stack.pop()
                    stack.append(val)
            if token == "-":
                if stack:
                    temp = stack.pop()
                    val = stack.pop() - temp
                    stack.append(val)
            if token == "/":
                if stack:
                    temp = stack.pop()
                    val = int(stack.pop() / temp)
                    stack.append(val)
        return int(stack[-1])