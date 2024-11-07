class Solution:

    def trap(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0

        # we only care whichever smaller
        # whichever smaller moves 
        while left < right:
            heightLeft = height[left]
            heightRight = height[right]
            if heightLeft > leftMax:
                leftMax = heightLeft
            if heightRight > rightMax:
                rightMax = heightRight

            minHeight = min(leftMax, rightMax)
            if (heightLeft < leftMax) and (heightLeft < rightMax):
                area += minHeight - heightLeft
                print('here', area, minHeight - heightLeft)
            if (heightRight < leftMax) and (heightRight < rightMax):
                area += minHeight - heightRight 

            if heightLeft <= heightRight: left += 1
            else: right -= 1
        

        return area
            
            
# Analysis
# Runtime: O(n)
# Space O(1)       
            