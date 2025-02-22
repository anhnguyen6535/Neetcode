class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        table = {}

        for charS in s:
            if charS in table:
                table[charS] += 1
            else:
                table[charS] = 1

        for charT in t:
            if not charT in table or table[charT] <= 0: return False
            table[charT] -= 1

        return True
