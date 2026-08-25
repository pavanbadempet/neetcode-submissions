class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"]":"[","}":"{",")":"("}
        stack = []
        for b in s:
            if b not in dic:
                stack.append(b)
            else:
                if not stack:
                    return False
                elif stack[-1] != dic.get(b):
                    return False
                stack.pop()
        if stack:
            return False
        return True