public class Solution {
    public bool IsValid(string s) {
        Stack<char> bracketStack = new Stack<char>();
        Dictionary<char, char> lookUpDict = new Dictionary<char, char>();
        lookUpDict.Add('}','{');
        lookUpDict.Add(')','(');
        lookUpDict.Add(']','[');
        
        foreach(char c in s){
            if (lookUpDict.ContainsKey(c)){
                if(bracketStack.Count>0){
                   char popped = bracketStack.Pop();
                    if (popped != lookUpDict[c]){
                        return false;
                    }else{
                        continue;
                    } 
                }else{
                    return false;
                }
                
            }else{
                bracketStack.Push(c);
            }
                
        }
        if(bracketStack.Count == 0){
            return true;
        }else{
            return false;
        }
        
    }
}