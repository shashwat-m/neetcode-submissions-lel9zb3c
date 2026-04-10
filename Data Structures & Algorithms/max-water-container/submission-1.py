class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = min(heights[left], heights[right]) * (right-left)
        temp_area = 0
        while left < right:
            
            temp_area = min(heights[left], heights[right]) * (right - left)
            area = max(area, temp_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return area