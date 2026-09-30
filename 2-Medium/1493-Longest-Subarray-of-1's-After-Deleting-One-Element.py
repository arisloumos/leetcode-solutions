class Solution(object):
    def longestSubarray(self, nums):
        start = end = zeros = max_length = 0
        while end < len(nums):
            if nums[end] == 0:
                zeros += 1
            while zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            length = end - start
            if length > max_length:
                max_length = length
            end +=1
        return max_length