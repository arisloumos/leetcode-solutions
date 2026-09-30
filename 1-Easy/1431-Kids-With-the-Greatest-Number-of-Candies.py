class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            result.append(total >= maxCandies)
        return result