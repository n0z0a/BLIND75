#NOT optimal, O(m + n) space. 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zero = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero.add((r, c))
        for i, j in zero:
            #set the column 
            for col in range(COLS):
                matrix[i][col] = 0
            for row in range(ROWS):
                matrix[row][j] = 0