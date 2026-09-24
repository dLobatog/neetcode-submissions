class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            elif c == ')':
                # pop a left paren if possible
                if len(left) > 0:
                    left.pop()
                # if not possible, possible to pop an star?
                elif len(star) > 0:
                    star.pop()
                else:
                    return False

        # print(left, star)
        while left and star:
            left_i = left.pop()
            star_i = star.pop()
            if star_i < left_i: # we pushed the left paren after star
                return False

        return len(left) == 0
                
