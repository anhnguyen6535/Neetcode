class Solution:

    # encode rule is like this:
    # len(str)#str
    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s

        return result

    # decode method:
    # read till # to find len(len(str))
    # convert to int
    # read the string according to the len(str)
    def decode(self, s: str) -> List[str]:
        result = []
        pointer = 0
        
        while pointer < len(s):
            count = pointer
            while s[count] != '#':
                count += 1
            lengthStr = int(s[pointer: count])   
            print(lengthStr)

            result.append(s[count + 1: lengthStr + count + 1])
            pointer = lengthStr + count + 1
        
        return result