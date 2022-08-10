class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        hashList = {}
        for i in nums:
            if i in hashList:
                return True
            else:
                hashList[i] = i
        return False

# what i learned:
# using the hash() function doesn' guarantee that each input will give a different output
# in my case hash(-1) = hash(-2) = -2