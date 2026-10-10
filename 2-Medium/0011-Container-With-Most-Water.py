class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while right > left:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
            if height[left] >= height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
        return max_area