class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = 0
        while pointer2 < len(nums):
            if nums[pointer2] != nums[pointer1]:
                pointer1 += 1
                nums[pointer1] = nums[pointer2]
            pointer2 += 1
        
        return pointer1+1