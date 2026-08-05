class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        numRows = len(matrix)
        numCols = len(matrix[0])
        result = [[0] * numRows for _ in range(numCols)]
        for r in range(numRows):
            for c in range(numCols):
                result[c][r] = matrix[r][c]
        return result
        