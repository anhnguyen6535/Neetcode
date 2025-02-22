class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Inputs: str s1 and s2
        # when true? char in s1 is next to each other in s2
        # when false? not all char s1 in s2, chars in s1 arent next to each other

        if len(s1) > len(s2): return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26


        for index in range(len(s1)):
            count_s2[ord(s2[index]) % ord('a')] += 1
            count_s1[ord(s1[index]) % ord('a')] += 1
        
        match = 26
        for index in range(26):
            if count_s1[index] != count_s2[index]: match -= 1


        if match == 26: return True
        for index in range(len(s1), len(s2)):
            new_chr_idx = ord(s2[index]) % ord('a')
            old_chr_idx = ord(s2[index - len(s1)]) % ord('a')
            if new_chr_idx == old_chr_idx: continue

            count_s2[new_chr_idx] += 1
            count_s2[old_chr_idx] -= 1

            
            if count_s2[new_chr_idx] == count_s1[new_chr_idx]: match += 1
            elif (count_s2[new_chr_idx] - 1 == count_s1[new_chr_idx]): match -= 1

            if count_s2[old_chr_idx] == count_s1[old_chr_idx]: match += 1
            elif (count_s2[old_chr_idx] + 1 == count_s1[old_chr_idx]): match -= 1
            
            if match == 26: return True


        return False
        