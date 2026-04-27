class Solution:
    TRANS = [
        [-1, 1, -1, 3],
        [0, -1, 2, -1],
        [3, 2, -1, -1],
        [1, -1, -1, 2],
        [-1, 0, 3, -1],
        [-1, -1, 1, 0]
    ]
    DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    START = [[1, 3], [0, 2], [2, 3], [1, 2], [0, 3], [0, 1]]

    def hasValidPath(self, grid: List[List[int]]) -> bool:       
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return True

        def check(d):
            if d == -1: return False
            r, c = self.DIRS[d]
            # O(1) Space
            while 0 <= r < m and 0 <= c < n:               
                d = self.TRANS[grid[r][c] - 1][d]
                if d == -1: return False
                if r == 0 and c == 0: return False
                if r == m - 1 and c == n - 1: return True
                
                dr, dc = self.DIRS[d] 
                r += dr
                c += dc
            return False

        a, b = self.START[grid[0][0] - 1]
        return check(a) or check(b)