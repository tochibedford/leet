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