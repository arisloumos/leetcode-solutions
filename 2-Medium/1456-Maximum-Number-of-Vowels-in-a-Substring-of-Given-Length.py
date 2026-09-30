class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u']
        total = 0
        for i in range(k):
            if s[i] in vowels:
                total += 1
        max_v = total
        for i in range(k, len(s)):
            if s[i] in vowels:
                total += 1
            if s[i-k] in vowels:
                total -= 1
            if total > max_v:
                max_v = total
        return max_v
        