class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a table stores index of groups in results
        # key to access the groups is the character in alphabet order
        # table = {(key, index of the corresponding array in results)}
        table = {}
        results = []

        # for each word, convert to list, sort in alphabet order
        # check if group exists in table
        # if yes, get the index, and append to that list in results
        # else, register in table, and create new list in results
        for word in strs:
            wordList = ''.join(sorted(list(word)))
            if wordList in table:
                results[table[wordList]].append(word)
            else:
                table[wordList] = len(results)
                results.append([word])

        return results
    
# Analysis:
# Sorting each word: log(m) with m is the word's length
# Sorting all word: m*log(m)
# Iterate throught the array of n words: O(n * mlog(m))
# =>>>> not bad but can do it better =>>> next we will look for O(n*m) solution


