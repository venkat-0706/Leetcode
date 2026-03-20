class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(grid) + 1, len(grid[0]) + 1
        ans = [[0] * (n - k) for _ in range(m - k)]
        if k == 1: return ans
        
        for row in range(m - k):
            subMat = SortedList(chain(*[grid[row + i][:k]       # <-- 1)
                                         for i in range(k)]))
        
            for col in range(n - k):
                
                diffs = [b - a for a, b in pairwise(subMat) if a != b]
                ans[row][col] = min(diffs, default = 0)         # <-- 2)
                
                if col == n - k - 1 : continue

                for i in range(k):
                    subMat.remove(grid[row + i][col])           # <-- 3)
                subMat.update([grid[row + i][col + k] for i in range(k)])

        return ans                                              # <-- 4)