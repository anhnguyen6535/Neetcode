import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []    # rank of frequency
        tables = {}     # hashMap of key: number and values: frequency

        for n in nums:
            if n in tables:
                tables[n] += 1
            else: tables[n] = 1

        for element in tables:
            heapq.heappush(minHeap,(-tables[element], element))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result
    
# Analysis
# iterate throught nums: len(nums) = m
# iterate throught tables: len(tables) = m (at most)
# print out: k
# O(m*k)