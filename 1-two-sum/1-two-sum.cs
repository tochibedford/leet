
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> subtracted = new Dictionary<int, int>();
        for(int i=0; i<nums.Length; i++){
            if(subtracted.ContainsKey(target-nums[i])){
                int[] index = {subtracted[target-nums[i]], i};
                return (index);
            } 
            else{
                if(subtracted.ContainsKey(nums[i])){
                    continue;
                }
                subtracted.Add(nums[i], i); 
            }     
        }
        
        int[] ind = {};
        return ind;
        
    }
}