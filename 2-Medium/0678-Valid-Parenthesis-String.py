class Solution(object):
    def checkValidString(self, s):
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            elif len(left) > 0:
                left.pop()
            elif len(star) > 0:
                star.pop()
            else:
                return False
        while len(left) > 0 and len(star) > 0:
            if star[-1] > left[-1]:
                left.pop()
                star.pop()
            else:
                return False
        return len(left) == 0