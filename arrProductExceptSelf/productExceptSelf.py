class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            result[i] *= product
        
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            result[i] *= product

        return result
    
# Analysis
# Go over the arr twice
# 1st: go forward to save product of prefixs
# 2nd: go backward to save product of postfixs
# =>>> O(2n) = O(n)