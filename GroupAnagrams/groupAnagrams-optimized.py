class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a table/dictionary stores 
        # key and array of anagram groups
        # key is the unique tuple of the character ascii sum in words
        table = {}

        # for each word, create a count array of character
        # since array cant be key, create tuple from it
        # if its in table, append word
        # else, register in table, and create new list 
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) % ord('a')] += 1
            if tuple(count) in table:
                table[tuple(count)].append(word)
            else:
                table[tuple(count)] = [word]

        return table.values()
    

## Analysis
#  Iterate throught all chars of each word len m: m
#  Do that for n words: O(m * n)