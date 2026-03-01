class Solution {
public:
    int minPartitions(string n) {
        int ans=0;
        for(int x:n){
            ans = max(ans,x-'0');
            if(ans==9){
                break;
            }
        }
        return ans;
    }
};