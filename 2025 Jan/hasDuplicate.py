class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate thru the array
        # check if the ele is in the set yet
        # if yes, return true
        # else, return false

        theSet = set()
        for num in nums:
            if num in theSet:
                return True
            theSet.add(num)
        
        # if no num is repeated then return False
        return False