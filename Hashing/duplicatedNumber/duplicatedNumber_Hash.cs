public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> aSet = new HashSet<int>();

        for (int i = 0; i < nums.Length;i++){
            if(aSet.Contains(nums[i])) return true;

            aSet.Add(nums[i]);
        }
        return false;
    }
}