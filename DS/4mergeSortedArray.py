class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        end = m+n-1
        m, n = m-1, n-1

        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end]  = nums2[n]
                n -= 1
            end -= 1
        while n>=0:
            nums1[end] = nums2[n]
            n -= 1
            end -= 1

        # take a number from num2
        # iterate over num1
        # check if the num2 number is higher of less than num1
        # move num1 iterator up by 1 if it is,
        # if the iterator has to come down by 1 at any point 
        # then it should insert the num2 number there and pick a new one from the num2 array
        # when it has reached the 0 portion it should just
                    

            

x = [1,2,3,0,0,0]
y = [2,5,6]

Solution().merge(x, 3, y, 3)
print(x)