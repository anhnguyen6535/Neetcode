class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ensure two words at the same length
        if(len(s) != len(t)): return False

        # create dictionary to store char occurence 
        table = {}
        for c in s:
            if c in table:
                table[c] = table[c] + 1
            else:
                table[c] = 1

        # if char c in t is in the dictionary, minus 1 occurence
        # if occurence = 0 or no char in dictionary at all, return false
        # if all char is found, return true
        for c in t:
            if c in table and table[c] > 0:
                table[c] = table[c] - 1
            else:
                return False
        return True

        