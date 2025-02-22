import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketList = [[] for _ in range(len(nums) + 1)]    # rank of frequency
        tables = {}     # hashMap of key: number and values: frequency

        # count frequency
        for n in nums:
            if n in tables:
                tables[n] += 1
            else: tables[n] = 1

        # add to bucket list
        # index is the frequency
        # bucketList[i] is the array of numbers that appear i times 
        for element in tables:
            bucketList[tables[element]].append(element)
        
        result = []
        for i in range(len(nums), 0, -1):
            for element in bucketList[i]:
                result.append(element)
            if len(result) == k:
                return result
            
## Analysis
## Count frequency: O(n)
## Add to bucketList: O(n)
## Create results: O(n)
## =>>>> O(n)