class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prev_col_w = [0] * (n+1) # [DP] prev col with prev col's score
        prev_col_wo = [0] * (n+1) # [DP] prev col without prev col's score
        if n == 1:
            return 0

        for j in range(1, n): # [LOOP] for each col
            cur_col_w = [0] * (n+1) # [DP] cur col with cur col's score
            cur_col_wo = [0] * (n+1) # [DP] cur col without cur col's score
            for i in range(n+1): # [LOOP] prev col (j-1) is black from row 0 to row i-1 (no black when i == 0)
                prev_col_val = 0 # prev col (j-1) score when prev black is i and cur black is k
                cur_col_val = 0 # cur col (j) score when prev black is i and cur black is k
                for p in range(i):
                    cur_col_val += grid[p][j]
                for k in range(n+1): # [LOOP] cur col (j) black is from row 0 to row k-1 (no black when k == 0)
                    if k > 0 and k <= i:
                        cur_col_val -= grid[k-1][j]
                    if k > i:
                        prev_col_val += grid[k-1][j-1]
                    cur_col_wo[k] = max(cur_col_wo[k], prev_col_val + prev_col_wo[i])
                    cur_col_wo[k] = max(cur_col_wo[k], prev_col_w[i])
                    cur_col_w[k] = max(cur_col_w[k], cur_col_val + prev_col_w[i])
                    cur_col_w[k] = max(cur_col_w[k], cur_col_val + prev_col_val + prev_col_wo[i])
            prev_col_w = cur_col_w
            prev_col_wo = cur_col_wo
        return max(cur_col_w)