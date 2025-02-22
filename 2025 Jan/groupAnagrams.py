from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate thru strs
        # for each str s,
        # modify a list of 26 ele corresponding to 26 alphabets
        # make a tuple of the list which acts as its identifier
        # add to a dict/set which keys are the tuple and value is a list of all strs belongs to that group

        theSet = defaultdict(list)
        for aStr in strs:
            count = [0]*26
            for charC in aStr:
                count[ord(charC) - ord('a')] += 1
            theSet[tuple(count)].append(aStr)

        return theSet.values()