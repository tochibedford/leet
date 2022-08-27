public class Solution {
    public int LengthOfLastWord(string s) {
        int total = 0;
        // int fC = 0;
        // find first index from behind that's not a space
//         for(int firstCharFromBehindIndex = s.Count()-1; firstCharFromBehindIndex>=0; firstCharFromBehindIndex--){
//             fC = firstCharFromBehindIndex;
//             if(s[firstCharFromBehindIndex] != ' '){
//                 break;
//             }
            
//         }
        // for(int i=fC; i>=0; i--){
        //     if(s[i] == ' ')
        //         break;
        //     total ++;
        // }
        s = s.Trim();
        for(int i=s.Count()-1; i>=0; i--){
            if(s[i] == ' ')
                break;
            total ++;
        }
        return total;
    }
}