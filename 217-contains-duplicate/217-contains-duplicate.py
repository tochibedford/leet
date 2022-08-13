class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashList = {}
        for i in nums:
            if i in hashList:
                return True
            else:
                hashList[i] = i
        return False