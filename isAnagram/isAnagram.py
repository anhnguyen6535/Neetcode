class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dictS = {}
        for charS in s:
            dictS[charS] = 1 + dictS.get(charS, 0)

        for charT in t:
            if charT in dictS:
                if dictS[charT] >= 1:
                    dictS[charT] -= 1
                else: return False
            else: return False
        return True
    
# Counter (s) = Counter(t)