class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for bracket in s:
            if bracket in ('(','[','{'):
                stack.append(bracket)
            else:
                if stack and dic[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False