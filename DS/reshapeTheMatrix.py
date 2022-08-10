import os

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # first check if it's even possible
        originalRows = len(mat)
        originalColumns = len(mat[0])
        newMatrix = []
        if originalRows * originalColumns != r * c or (originalColumns==c and originalRows==r):
            return mat
        if originalColumns/c > 1:
            # for column reduction/row increase
            for row in mat:
                for segment in range(int(originalColumns/c)):
                    newMatrix.append(row[segment*c:(segment+1)*c])
        elif originalColumns/c < 1:
            # for row reduction/column increase
            colSegment = int(originalRows/r)
            for i in range(r):
                subRow = []
                for j in range(i*colSegment, (i+1)*colSegment):
                    subRow.extend(mat[j])
                newMatrix.append(subRow)
        return newMatrix
        

os.system('cls')
# Test 1
try:
    assert Solution().matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]
    print("Test 1 passed\n")
except AssertionError:
    print("Test 1 failed")
    print(f"For Test 1: Expected {[[1,2,3,4]]} got {Solution().matrixReshape([[1,2],[3,4]], 1, 4)}\n")

# Test 2
try:
    assert Solution().matrixReshape([[1,2],[3,4]], 2, 4) == [[1,2],[3,4]]
    print("Test 2 passed\n")
except AssertionError:
    print("Test 2 failed")
    print(f"For Test 2: Expected {[[1,2],[3,4]]} got {Solution().matrixReshape([[1,2],[3,4]], 1, 4)}\n")

# Test 3
try:
    assert Solution().matrixReshape([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ], 8, 2) == [
            [1,2],
            [3,4],
            [5,6],
            [7,8],
            [9,10],
            [11,12],
            [13,14],
            [15,16]]
    print("Test 3 passed\n")
except AssertionError:
    print("Test 3 failed")
    print(f"For Test 3: Expected {[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]]} got {Solution().matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 8, 2)}\n")

# Test 4
try:
    assert Solution().matrixReshape([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ], 2, 8) == [
            [1,2,3,4,5,6,7,8],
            [9,10,11,12,13,14,15,16]]
    print("Test 4 passed\n")
except AssertionError:
    print("Test 4 failed")
    print(f"For Test 4: Expected {[[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]]} got {Solution().matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 8)}\n")