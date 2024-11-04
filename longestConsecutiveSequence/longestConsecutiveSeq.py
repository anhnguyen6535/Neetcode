class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        maxLength = 0

        for i in range(len(nums)):
            n = nums[i]
            if (n-1) not in table:
                length = 1
                j = n+1
                while (j) in table:
                    length += 1
                    j += 1
                if length > maxLength: maxLength = length
                i += length

        return maxLength
            