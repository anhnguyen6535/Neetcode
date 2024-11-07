class Solution:
    # def isLocalMax(self, height: List[int], right: int):
    #     # print(right, height[right])
    #     if (right == 0 or right >= (len(height)-1)): return False
    #     if (height[right] > height[right-1]) and (height[right] >= height[right+1]):
    #         return True
    #     return False

    def isLocalMax(self, height: List[int], right: int, left: int) -> int:
        # print(right, height[right])
        # if (right == 0 or right >= (len(height)-1)): return False
        if (right == 0): return 1
        # if (height[right] > height[right-1]) and (height[right] >= height[right+1]):
        while (height[right] > height[right-1]) and (height[right] >= height[right+1]) and (height[right] >= height[left]) and right < len(height) - 1:
            right += 1
            # return True
        print(right)
        return right

    def trap(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = 0

        # for i in range(1):
        while right < (len(height) - 1):
            # if not self.isLocalMax(height, right, left) and right < len(height) - 1:
            #     right += 1
            #     continue

            right = self.isLocalMax(height, right, left)
            
            minHeight = min(height[left], height[right])
            left += 1
            while left < right:
                area += minHeight - height[left]
                print(left, right,area)
                left += 1

            right += 1
        return area
            

# Analysis
# Runtime: O(n)
# Space O(n)       
                  
            