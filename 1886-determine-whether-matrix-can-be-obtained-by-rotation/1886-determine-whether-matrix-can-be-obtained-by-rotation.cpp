class Solution {
public:
    static bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        const int n=mat.size();
        bitset<4> rot90=15;
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++){
                rot90[0]=rot90[0] & (mat[i][j]==target[i][j]);
                rot90[1]=rot90[1] &(mat[j][n-1-i]==target[i][j]);
                rot90[2]=rot90[2] &(mat[n-1-i][n-1-j]==target[i][j]);
                rot90[3]=rot90[3] &(mat[n-1-j][i]==target[i][j]);
            }
        return rot90!=0;
    }
};