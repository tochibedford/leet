class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        i = 0
        currentLetter = 0
        prefix = ''
        while True:
            # try:
            while i < len(strs)-1:
                if strs[i][currentLetter] != strs[i+1][currentLetter]:
                    break
                elif strs[i][currentLetter] == strs[i+1][currentLetter] and i == len(strs)-2:
                    print(strs[i][currentLetter])
                    prefix += strs[i][currentLetter]
                i+=1
            currentLetter += 1
            # except IndexError:

            #     break
            
            

print(Solution().longestCommonPrefix(["hey", "heya"]))