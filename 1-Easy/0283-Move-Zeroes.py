class Solution(object):
    def moveZeroes(self, nums):
        i = c = 0
        while i < len(nums):
            if nums[i] == 0:
                if i == len(nums) - c:
                    return
                del nums[i]
                nums.append(0)
                c += 1
            else:
                i += 1