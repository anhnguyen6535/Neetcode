class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''

        for aStr in strs:
            encodedStr += str(len(aStr)) + '%' + aStr

        return encodedStr
       
    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0

        while (i < len(s)):
            counter = ''
            while s[i] != '%':
                counter += s[i]
                i += 1
            i += 1  # go pass '%' char
            
            decodedList.append(s[i: i + int(counter)])
            i += int(counter)
        
            
        return decodedList