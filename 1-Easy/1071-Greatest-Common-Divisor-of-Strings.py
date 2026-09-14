class Solution(object):
    def gcd(self, num1, num2):
        a, b = max(num1, num2), min(num1, num2)
        while b != 0:
            res = a % b
            a, b = b, res
        return a

    def gcdOfStrings(self, str1, str2):
        if str1+str2 != str2+str1:
            return ""
        
        prefix = self.gcd(len(str1), len(str2))
        return str1[:prefix]