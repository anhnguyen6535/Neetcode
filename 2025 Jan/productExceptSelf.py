class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First, multiply number from left to right, put the res in the next cell
        # Then, multiply number from right to left, put the res in the next cell

        theList = [1]*len(nums)
        total = 1

        # multiply from left to right
        for i in range (len(nums)-1):
            total *= nums[i]
            theList[i+1]  = total

        total = 1
        for i in range(len(nums)-1, 0, -1):
            total *= nums[i]
            theList[i-1] *= total

        return theList