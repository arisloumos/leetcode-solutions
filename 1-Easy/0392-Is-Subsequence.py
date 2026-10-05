class Solution(object):
    def isSubsequence(self, s, t):
        left = right = 0
        if s == "":
            return True
        else:
            while right <= len(t)-1:
                if t[right] == s[left]:
                    left += 1
                    if left == len(s):
                        return True
                right += 1
        return False