'''
Given an n x n matrix rotate the matrix clockwise
While not creating any additional space (In-Place)
Example 1:
123      741
456 -->  852
789      963
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Horizontal Reflection
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1],  matrix[i][j]
        return matrix