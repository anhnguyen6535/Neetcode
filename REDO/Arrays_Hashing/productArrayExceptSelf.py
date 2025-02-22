class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productRes = [1]*(len(nums))

        leftProd = 1
        for i in range(len(nums)-1):
            leftProd *= nums[i]
            productRes[i + 1] *= leftProd

        rightProd = 1
        for i in range(len(nums)-1, 0, -1):
            rightProd *= nums[i]
            productRes[i - 1] *= rightProd

        return(productRes) 
           