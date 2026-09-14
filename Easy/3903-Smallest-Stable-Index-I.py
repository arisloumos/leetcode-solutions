class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            instability = max(nums[0:i+1]) - min(nums[i:])
            if instability <= k:
                return i
        return -1