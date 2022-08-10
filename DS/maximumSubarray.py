class Solution:
    def maxSubArray(self, nums: list) -> int:
        maxTotal = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            maxTotal = max(maxTotal, currentSum)
        return maxTotal 
        