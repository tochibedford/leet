from math import floor

class Solution:
    def rowSearch(self) -> int:
        low = 0
        high = len(self.matrix)-1
        mid = floor((low+high)/2)
        if self.target < self.matrix[low][-1]:
            return 0
        elif self.target > self.matrix[high][-1]:
            return False

        while low <= high - 1:
            if self.matrix[low][-1] == self.target or self.matrix[mid][-1]==self.target or self.matrix[high][-1] == self.target:
                return True
            else:
                if self.target > self.matrix[mid][-1]:
                    low = mid+1
                    mid = floor((low+high)/2)
                elif self.target < self.matrix[mid][-1]:
                    high = mid
                    mid = floor((low+high)/2)          
        return high
    
    def columnSearch(self) -> bool:
        low = 0
        high = self.n
        mid = floor((low+high)/2)
        while low < high:
            if self.matrix[self.selectedRow][low] == self.target or self.matrix[self.selectedRow][mid]==self.target or self.matrix[self.selectedRow][high] == self.target:
                return True
            else:
                if self.target > self.matrix[self.selectedRow][mid]:
                    low = mid + 1
                    mid = floor((low+high)/2)
                elif self.target < self.matrix[self.selectedRow][mid]:
                    high = mid - 1
                    mid = floor((low+high)/2)
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        self.matrix = matrix
        self.target = target
        self.n = len(self.matrix[0])-1

        if len(self.matrix) == 1 and len(self.matrix[0]) == 1 and self.matrix[0][0] == self.target:
            return True
        elif len(self.matrix) == 1 and len(self.matrix[0]) == 1 and self.matrix[0][0] != self.target:
            return False
            
        self.selectedRow = self.rowSearch()
        if self.selectedRow == True and type(self.selectedRow) == type(True):
            return True
        return self.columnSearch()
        
# leet problem 74.
# This program runs 2 parallel binary searches on a 2D array :
#  from the constraints we are always sure that the array rows and columns are sorted
# 1 to find the row of the target, and once it has found the targets suspected row in the array, 
# it does a regular 3 pointer binary search on that row to check if the target exists, returning True if it does, and False if it doesn't

matrix = [[1, 1], [2,4]]
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16
print(Solution().searchMatrix(matrix2, target))

target = 2
print(Solution().searchMatrix(matrix, target))