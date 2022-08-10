# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         # numsLessThanTargets = list(filter(lambda x: x<=target, nums))
#         # since theres only 1 solution
#         for index, i in enumerate(nums):
#             subTarget = target-i
#             for jindex, j in enumerate(nums):
#                 if index == jindex:
#                     continue
#                 if subTarget == j:
#                     return [index, jindex]
#                 else:
#                     pass

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        mapper = dict()
        for index, i in enumerate(nums):
            subTarget = target-i
            if subTarget in mapper:
                return mapper[subTarget], index
            else:
                mapper[i] = index

solution = Solution()
print(solution.twoSum([-1,-2,-3,-4,-5], -8))


'''
using hash maps
subtract cuurent number from target
if subTarget is in mapper return value of subTarget key in mapper
else just add subtarget to mapper in the form subTarget:index
'''
