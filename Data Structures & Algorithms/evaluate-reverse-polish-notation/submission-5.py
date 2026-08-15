import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set()
        ops.add('+')
        ops.add('-')
        ops.add('*')
        ops.add('/')
        for token in tokens:
            # print(stack)
            if token not in ops:
                # stack up
                stack.append(int(token))
            else:
                # pop 2 and do operation
                r, l = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(l + r)
                elif token == '-':
                    stack.append(l - r)
                elif token == '*':
                    stack.append(l * r)
                elif token == '/':
                    stack.append(int(l /r))
                else:
                    raise Error('wrong token')

        # print(stack)
        return stack[-1]

