class Solution(object):
    def reverseWords(self, s):
        words =  s.split()
        res = ""
        
        while len(words) > 0:
            res += words.pop()
            if len(words) > 0:
                res += " "

        return res