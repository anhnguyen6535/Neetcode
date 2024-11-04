class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary store index and 
        # the amount of value the number at that index needs to create the target
        table = {}

        # if number n is in table, it means table[n] is the index of the complement number
        # return index of n and table[n]
        # otherwise, save offset of target - n in the table
        for i in range (len(nums)):
            if nums[i] in table:
                return([table[nums[i]], i])
            else:
                offset = target - nums[i]
                table[offset] = i

        return


        