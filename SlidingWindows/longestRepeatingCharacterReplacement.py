class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Slide window to find num of replacement
        res = 0
        count = {}
        start = 0
        end = 0
        maxCount = 0

        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            maxCount = max(maxCount, count[s[end]])

            while (end - start  + 1) - maxCount > k:
                count[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)
        return(res)
    

# O(26n)
# import heapq

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         # Slide window to find num of replacement
#         res = 0
#         # for curChar in string.ascii_uppercase:
#         for curChar in range (ord('A'), ord('Z')+1):
#             imposter = []
#             token = 0
#             numEle = 0
#             start = 0

#             for index, charA in enumerate(s):
#                 if charA == chr(curChar):
#                     numEle += 1
#                 else:
#                     heapq.heappush(imposter, index)
#                     if token < k:
#                         token += 1
#                         numEle += 1
#                     else:
#                         newStart = heapq.heappop(imposter) + 1
#                         numEle -= newStart - start - 1
#                         start = newStart
                
#                 res = max(numEle, res)
#         return(res)

