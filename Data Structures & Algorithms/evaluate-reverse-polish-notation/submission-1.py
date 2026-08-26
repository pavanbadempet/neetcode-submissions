class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2-t1)
            elif t == '*':
                stack.append(stack.pop()*stack.pop())
            elif t == '/':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(t2/t1))
            else:
                stack.append(int(t))
        return stack[-1]