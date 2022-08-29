public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if(strs.Length == 1){
            return strs[0];
        }
        string sub = "";
        for(int i=0; i<200; i++){
            try{
                char currChar = strs[0][i];
                for(int j=1; j<strs.Length; j++){
                    if(currChar != strs[j][i]){
                        return sub;
                    }else{
                        if(j == strs.Length-1){
                            sub += currChar;
                        }
                    }
                }
            }catch(IndexOutOfRangeException e){
                return sub;
            }
            
        }
        
        return sub;
        
    }
}