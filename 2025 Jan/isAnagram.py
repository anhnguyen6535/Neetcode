from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first, make sure string s and t are at the same length
        # create a dict theDict
        # iterate thru string s, update theDict:
        #   if char is in theDict, ++ occurrence
        #   else, theDict[char] = 1
        # iterate thru string t, update theDict:
            # if char is not in theDict or theDict[char] = 0: return False
            # else theDict[char] --

        if len(s) != len(t): return False

        theDict = defaultdict(int)

        for charS in s:
            theDict[charS] += 1

        for charT in t:
            if theDict[charT] <= 0: return False
            theDict[charT] -= 1

        # since all char in t was found in theDict, return True
        return True