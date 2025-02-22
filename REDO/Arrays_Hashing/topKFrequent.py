class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCounter = {}
        maxCount = 0

        for num in nums:
            if num in frequencyCounter:
                frequencyCounter[num] += 1
            else: 
                frequencyCounter[num] = 1

            if frequencyCounter[num] > maxCount: maxCount = frequencyCounter[num]

        bucketList = [[] for _ in range(len(nums) + 1)]
        for ele, key in frequencyCounter.items():
            bucketList[key].append(ele)

        res = []
        for i in range(maxCount, 0, -1):
            for ele in bucketList[i]:
                res.append(ele)
                if len(res) == k:
                    return res

        return res
    
# O(N log N)    
# import heapq

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequencyCounter = {}

#         for num in nums:
#             if num in frequencyCounter:
#                 frequencyCounter[num] -= 1

#             else: 
#                 frequencyCounter[num] = -1

#         aHeap = []

#         for ele, key in frequencyCounter.items:
#             heapq.heappush(aHeap, (key, ele))
        
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop()[1])

#         return res