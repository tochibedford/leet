/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */
// 1,2,3,4,5,6,7,8,9
public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        int low = 1;
        int high = n;
        int middle = (int) (low + (high-low)/2);
        if(n==1){
            return 1;
        }
        while(low < high){
            if(!IsBadVersion(middle)){
                low = middle +1;
            }else{
                high = middle;
            }
            middle = (int) (low + (high-low)/2);
        }
        return low;
        
    }
}