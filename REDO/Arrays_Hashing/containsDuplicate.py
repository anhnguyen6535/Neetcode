class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = set()

        for num in nums:
            if num in table: return True
            table.add(num)

        return False