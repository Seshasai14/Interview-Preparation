class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[0 for i in range(len(matrix))]
        col=[0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(row[i] or col[j]==1):
                    matrix[i][j]=0
        return matrix


        