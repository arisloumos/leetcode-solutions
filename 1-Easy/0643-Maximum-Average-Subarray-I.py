class Solution(object):
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        max_avg = float(total) / k
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            avg = float(total) / k
            if avg > max_avg:
                max_avg = avg
        return max_avg