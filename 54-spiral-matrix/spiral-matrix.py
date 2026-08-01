class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        for r in range(rows):
            for c in range(cols):
                print("curre", matrix[r][c])