class Solution(object):
    def countCommas(self, n):
        if n <= 999:
            return 0
        else:
            return n-999