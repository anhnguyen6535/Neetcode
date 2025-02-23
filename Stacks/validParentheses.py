class Solution:
    def isValid(self, s: str) -> bool:
        # when is true?
        # put in a heapq first in last out
        # everytime encounter on of the closing, pop the most current opening
        # if matched, continue
        # else return False

        listOpening = []
        mapOpenClose = {")" : "(", "}" : "{", "]" : "["}

        for charA in s:
            if charA in mapOpenClose:
                if listOpening and listOpening[-1] == mapOpenClose[charA]: 
                    listOpening.pop()
                else: return False
            else:
                listOpening.append(charA)

        return len(listOpening) == 0