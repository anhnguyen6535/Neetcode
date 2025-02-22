   
# O(N * K)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for aStr in strs:
            count = [0]*26

            for charS in aStr:
                count[ord(charS) % ord('a')] += 1

            # list is unhashable
            if tuple(count) in table:
                table[tuple(count)].append(aStr)
            else:
                table[tuple(count)] = [aStr]

        return table.values
    
# O(N * KlogK)    
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         table = {}
#         listTable = []
#         for str in strs:
#             tempStr = ''.join(sorted(str))
#             if tempStr in table:
#                 listTable[table[tempStr]].append(str)

#             else:
#                 table[tempStr] = len(listTable)
#                 listTable.append([str])

#         return listTable