from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a bucket list storing with index indicates the frequency
        # for example theList[1] = [a, b] => number a and b occurs once 
        # in the end, loop thru theList from last to first to get k eles

        count = [[] for _ in range(len(nums)+1)]
        theHash = defaultdict(int)  # this store the frequency

        for num in nums:
            theHash[num] += 1

        print(theHash)
        for num, freq in theHash.items():
            count[freq].append(num)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for ele in count[i]:
                res.append(ele)
                if len(res) == k: return res
