short dp[200][200][1001];
class Solution {
public:
    int k;
    const short NO=SHRT_MIN;
    int f(int i, int j, int c, vector<vector<int>>& grid){
        if (i<0 || j<0 || c>k) return NO;
        if (dp[i][j][c]!=-1) return dp[i][j][c];
        int x=grid[i][j], cost=c+(x!=0);
        if (cost>k) 
            return dp[i][j][c]=NO;
        if (i==0 && j==0)
            return dp[i][j][c]=grid[0][0];
        return dp[i][j][c]=x+max(f(i-1, j, cost, grid), f(i, j-1, cost, grid));
    }
    int maxPathScore(vector<vector<int>>& grid, int k) {
        this->k=k;
        const int row=grid.size(), col=grid[0].size();
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
                memset(dp[i][j], -1, (k+1)*sizeof(short));
        int ans=f(row-1, col-1, 0, grid);
        return ans<0?-1:ans;
    }
};

const auto init = []() noexcept {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();