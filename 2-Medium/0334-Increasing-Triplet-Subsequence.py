class Solution(object):
    def increasingTriplet(self, nums):
        m1 = float("inf")
        m2 = float("inf")
        for i in range(len(nums)):
            if nums[i] > m2:
                return True
            if nums[i] < m2 and nums[i] > m1:
                m2 = nums[i]
            if nums[i] < m1:
                m1 = nums[i]
        return False