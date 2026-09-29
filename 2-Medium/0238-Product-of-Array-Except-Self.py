class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        right_prod = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_prod *= nums[i+1]
            answer[i] *= right_prod
        return answer