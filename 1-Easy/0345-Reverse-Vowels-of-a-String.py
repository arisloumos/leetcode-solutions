class Solution(object):
    def reverseVowels(self, s):
        targets = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        found = []
        sol = ""

        for i in range(len(s)):
            if s[i] in targets:
                found.append(s[i])
        
        for i in range(len(s)):
            if s[i] in targets:
                sol += found.pop()
            else:
                sol += s[i]
        
        return sol