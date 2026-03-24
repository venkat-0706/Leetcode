class Solution {
public:
    static vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        const int N=12345, n=grid.size(), m=grid[0].size();
        vector<vector<int>> ans(n, vector<int>(m));
        uint64_t pref=1, suf=1;
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++){
                ans[i][j]=pref;
                pref=pref*grid[i][j]%N;
            }
        for(int i=n-1; i>=0; i--)
            for(int j=m-1; j>=0; j--){
                ans[i][j]=ans[i][j]*suf%N;
                suf=suf*grid[i][j]%N;
            }
        return ans;
    }
};