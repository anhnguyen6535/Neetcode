class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate thru nums
        # check in theSet if its counterpart to target has been found yet
        # if yes, return True
        # else, theSet.add(target-num)

        theSet = {}

        for i, num in enumerate(nums):
            if num in theSet:
                return [theSet[num], i]
            theSet[target-num] = i

        # cant find any pair
        return []