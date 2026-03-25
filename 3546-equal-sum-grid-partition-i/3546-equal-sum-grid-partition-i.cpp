class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<long long> rowSum(n, 0);
        vector<long long> colSum(m, 0);

        long long total = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                rowSum[i] += grid[i][j];
                colSum[j] += grid[i][j];
                total += grid[i][j];
            }
        }

        for(int i = 0; i < n; i++) {
            if(i>0)rowSum[i] += rowSum[i-1];
        }
        for(int i = 0; i < m; i++) {
            if(i>0)colSum[i] += colSum[i-1];
        }

        for(auto x : rowSum) {
            if(x == total-x) return true;
        }
        for(auto x : colSum) {
            if(x == total-x) return true;
        }

        return false;
    }
};