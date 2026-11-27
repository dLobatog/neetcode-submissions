class Solution:
    def decodeString(self, s: str) -> str:
        # when a "]" is found, pop until "[" and then pop 1 more for "k"
        stack = []
        result = []
        for c in s:
            if c == ']':
                sequence = []
                cur = ''
                while cur != '[':
                    cur = stack.pop()
                    sequence.append(cur)
                # print(''.join(sequence[::-1]))
                sequence = sequence[::-1][1:] # remove the '[' and reverse 
                k = []
                while stack and stack[-1].isnumeric():
                    k.append(stack.pop()) # get k - but it might be many digits
                k = int(''.join(k[::-1]))
                for _ in range(k):
                    stack.append(''.join(sequence))
            else:
                stack.append(c)
        return ''.join(stack)
