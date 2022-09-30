class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums[:] = [i for i in nums if i != val]
        # return len(nums)
        occurences = 0
        pointer = 0
        while pointer<len(nums):
            if nums[pointer] == val:
                occurences += 1
            else:
                nums[pointer - occurences] = nums[pointer]
            pointer += 1
        return len(nums) - occurences