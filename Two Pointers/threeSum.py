class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # since we dont want duplicate triplet, we skip numbers if we already calculate
        # to do that, we first sort it
        nums.sort()

        # if num > 0, since sorted, no more possible set to 0
        # if num was calculated, skip
        # now do two pointer to find the other two nums
        # if left is already seen, skip
        for i in range (len(nums)):
            if nums[i] > 0: break

            if (i > 0) and (nums[i-1] == nums[i]):
                continue

            # perform two sum
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total > 0: 
                    right -= 1
                elif total < 0: 
                    left += 1
                else: 
                    print(left, right, nums[left], nums[right])
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return result
