class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let track = new Map()
        let maxLength = 0
        let start = 0

        for (let i = 0; i < s.length; i ++){
            if(track.has(s[i]) && track.get(s[i]) >= start){
                start = track.get(s[i]) + 1
            }

            track.set(s[i], i)
            maxLength = Math.max(maxLength, i - start+1)
        }

        return maxLength
    }
}
