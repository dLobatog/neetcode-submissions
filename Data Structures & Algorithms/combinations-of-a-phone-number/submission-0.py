class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # on each number, you hap it to 3-4 letters
        num_to_s = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        result = set()

        def bt(i, s):
            if i == len(digits):
                if s != '':
                    result.add(s)
                return
            
            options = num_to_s[int(digits[i])]
            for c in options:
                bt(i+1, s + c)

        bt(0, '')
        return [s for s in result]

