class Solution(object):
    def countCommas(self, n):
        if n < 10**3:
            return 0
        elif n < 10**6:
            return n - 10**3 + 1
        elif n < 10**9:
            return 10**6 - 10**3 + (n - 10**6 + 1) * 2
        elif n < 10**12:
            return 10**6 - 10**3 + (10**9 - 10**6) * 2 + (n - 10**9 + 1) * 3
        elif n < 10**15:
            return 10**6 - 10**3 + (10**9 - 10**6) * 2 + (10**12 - 10**9) * 3 + (n - 10**12 + 1) * 4
        else:
            return 10**6 - 10**3 + (10**9 - 10**6) * 2 + (10**12 - 10**9) * 3 + (10**15 - 10**12) * 4 + 1 * 5