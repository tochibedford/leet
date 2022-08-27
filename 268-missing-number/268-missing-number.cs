public class Solution {
    public int MissingNumber(int[] nums) {
        int sum = ((nums.Length+1)*nums.Length)/2;
        
        for(int i = 0; i<=nums.Length-1; i++){
            sum -= nums[i];
        }
        return sum;
    }
}