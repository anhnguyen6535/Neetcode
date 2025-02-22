public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        Dictionary<char, int> dict = new Dictionary<char, int>();

        foreach (char c in s){
            if(dict.ContainsKey(c)) dict[c] += 1;
            else dict.Add(c, 1);
        }

        foreach (char c in t){
            if(dict.ContainsKey(c))
                if(dict[c] >= 1) dict[c] -= 1;
                else return false;
            else return false;
        }
        
        return true;
                
    }
}
