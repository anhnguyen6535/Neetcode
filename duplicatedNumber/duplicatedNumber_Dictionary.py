class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aSet = set()
        for n in nums:
            if n in aSet: return True
            aSet.add(n)
        return False