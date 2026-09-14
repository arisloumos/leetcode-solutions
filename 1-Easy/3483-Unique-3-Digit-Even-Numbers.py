class Solution(object):
    def totalNumbers(self, digits):
        numbers = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and j != k and digits[i] != 0:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if number % 2 == 0:
                            numbers.add(number)
        return len(numbers)