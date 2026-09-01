class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']

        if n == 2:
            # add@0. add@1
            return ['()()', '(())']

        result = set()
        prev = self.generateParenthesis(n-1)
        for i in range(len(prev)):
            # insert at all positions
            for j in range(len(prev[i])):
                cand = prev[i][:j] + '()' + prev[i][j:]
                result.add(cand)

        return list(result)
