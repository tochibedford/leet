class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        # algorithm 1
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             intersection.append(nums1[i])
        #             nums1[i] = -1
        #             nums2[j] = -2
        #             break

        #  algorithm 2
        # if len(nums2)>=len(nums1):
        for i in nums1:
            try:
                existsAt = nums2.index(i)
                intersection.append(i)
                nums2[existsAt] = -1
            except ValueError:
                continue

        return intersection



assert sorted(Solution().intersect([1,2,2,1], [2,2])) == sorted([2,2]), f"Got '{Solution().intersect([1,2,2,1], [2,2])}' expected {[2,2]} in any order"
assert sorted(Solution().intersect([4,9,5], [9,4,9,8,4])) == sorted([4,9]), f"Got '{Solution().intersect([4,9,5], [9,4,9,8,4])}' expected {[4,9]} in any order"
assert sorted(Solution().intersect([1,2,2,2], [2,2,1])) == sorted([2,2,1]), f"Got '{Solution().intersect([1,2,2,2], [2,2,1])}' expected {[2,2,1]} in any order"
assert sorted(Solution().intersect([1,2,2,1], [1])) == sorted([1]), f"Got '{Solution().intersect([1,2,2,1], [1])}' expected {[1]} in any order"

print(f"Got '{Solution().intersect([1,2,2,1], [2,2])}' expected {[2,2]} in any order")
print(f"Got '{Solution().intersect([4,9,5], [9,4,9,8,4])}' expected {[4,9]} in any order")
print(f"Got '{Solution().intersect([1,2,2,2], [2,2,1])}' expected {[2,2,1]} in any order")
print(f"Got '{Solution().intersect([1,2,2,1], [1])}' expected {[1]} in any order")