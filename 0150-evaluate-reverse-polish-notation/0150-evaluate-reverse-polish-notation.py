from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                b,a = stack.pop(), stack.pop()
                if i=='/': stack.append(str(int(int(a)/int(b))))
                else: stack.append(str(eval(a+i+b)))
        return int(stack[0])
                    
            