class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        sumX = [0] * cols
        sumY = [0] * cols
        res = 0

        for i in range(rows):
            rx = 0
            ry = 0
            for j in range(cols):
                if grid[i][j] == 'X':
                    rx += 1
                elif grid[i][j] == 'Y':
                    ry += 1
                
                sumX[j] += rx
                sumY[j] += ry
                
                if sumX[j] > 0 and sumX[j] == sumY[j]:
                    res += 1

        return res