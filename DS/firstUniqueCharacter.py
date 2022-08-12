class Solution:
    def charChecker(self, charList):
        if len(charList) == 1:
            return charList
    def firstUniqChar(self, s: str) -> int:
        characterMap = dict()
        for index, char in enumerate(s):
            try:
                if characterMap[char]:
                    characterMap[char].append(index)
            except KeyError:
                characterMap[char] = [index]
        singleCharacters = list(filter(self.charChecker, characterMap.values()))
        if singleCharacters:
            return min(singleCharacters)[0]
        
        return -1




print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))