class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxAreaVal = 0

        while left < right:
            area = min(heights[left], heights[right])*(abs(right-left))
            if (area > maxAreaVal): maxAreaVal = area

            # Move whichever smaller
            if heights[left] <= heights[right]:
                left += 1
            
            elif heights[right] < heights[left]:
                right -= 1

        return maxAreaVal