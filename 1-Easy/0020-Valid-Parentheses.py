class Solution(object):
    def isValid(self, s):
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{' }
        stack = []
        for i in range(len(s)):
            if s[i] in pairs.values():
                stack.append(s[i])
            elif len(stack) != 0 and stack[-1] == pairs[s[i]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0