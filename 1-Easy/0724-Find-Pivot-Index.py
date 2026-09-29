class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
            else:
                left_sum += nums[i-1]
            
            if i == len(nums)-1:
                right_sum = 0
            else:
                right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i
        return -1