class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')' or char == ']' or char == '}':
                if len(stack) != 0:
                    if match[char] != stack[-1]:
                        return False
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
            