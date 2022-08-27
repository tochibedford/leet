public class Solution {
    public int MissingNumber(int[] nums) {
//      sum of first n nubers in an AP === n/2 × [2a + (n-1)d]
        int sum = ((nums.Length+1)*nums.Length)/2;
        for(int i = 0; i<=nums.Length-1; i++){
            sum -= nums[i];
        }
        return sum;
    }
}