class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k >> 1):
            row1 = grid[x + i]
            row2 = grid[x + k - 1 - i]
            for j in range(k):
                row1[y + j], row2[y + j] = row2[y + j], row1[y + j]
        
        return grid