public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        Dictionary<int, int> hashDict = new Dictionary<int, int>();
        List<int> finalArray = new List<int>();
        for(int i = 0; i<=nums1.Length-1; i++){
            if(!hashDict.ContainsKey(nums1[i])){
                hashDict.Add(nums1[i], i);
            }
        }
            
        for(int j = 0; j<=nums2.Length-1; j++){
            if(hashDict.ContainsKey(nums2[j])){
                finalArray.Add(nums2[j]);
                hashDict.Remove(nums2[j]);
            }
        }
        
        return finalArray.ToArray();
    }
}