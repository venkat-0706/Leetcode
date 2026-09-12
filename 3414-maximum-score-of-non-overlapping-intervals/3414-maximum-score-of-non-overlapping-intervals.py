class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        arr.sort(key=lambda x: x[1])
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            
            low, high = 1, i - 1
            prev = 0
            while low <= high:
                mid = (low + high) // 2
                if arr[mid - 1][1] < l:
                    prev = mid
                    low = mid + 1
                else:
                    high = mid - 1
                    
            for k in range(1, 5):
                skip_w, skip_idx = dp[i - 1][k]
                
                prev_w, prev_idx = dp[prev][k - 1]
                take_w = prev_w + w
                take_idx = sorted(prev_idx + [idx])
                
                if take_w > skip_w:
                    dp[i][k] = (take_w, take_idx)
                elif take_w == skip_w:
                    if take_idx < skip_idx:
                        dp[i][k] = (take_w, take_idx)
                    else:
                        dp[i][k] = (skip_w, skip_idx)
                else:
                    dp[i][k] = (skip_w, skip_idx)
                    
        return dp[n][4][1]