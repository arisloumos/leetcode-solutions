class Solution(object):
    def removeStars(self, s):
        i = 0
        stack = []
        while i <= len(s)-1:
            if s[i] != '*':
                stack.append(s[i])
            elif len(stack) > 0:
                stack.pop()
            i += 1
        return "".join(stack)