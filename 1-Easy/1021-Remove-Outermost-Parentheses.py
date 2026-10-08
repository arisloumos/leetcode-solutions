class Solution(object):
    def removeOuterParentheses(self, s):
        first = True
        c1 = c2 = i = 0
        while i < len(s):
            if first:
                first = False
                s = s[:i] + s[i+1:]
            elif s[i] == '(':
                c1 += 1
                i +=1
            elif s[i] == ')':
                if c1 != c2:
                    c2 += 1
                    i +=1
                else:
                    first = True
                    s = s[:i] + s[i+1:]
        return s