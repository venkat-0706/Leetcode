class Solution {
public:
    static constexpr int mod=1e9+7;
    inline static void apply_q(vector<int>& nums, auto& q){
        const int l=q[0], r=q[1], k=q[2], v=q[3];
        for(int i=l; i<=r; i+=k){
            long long x=nums[i];
            x*=v;
            if (x>=mod) x%=mod;
            nums[i]=x;
        }
    }
    static int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        for(auto& q: queries)
            apply_q(nums, q);
        return accumulate(nums.begin(), nums.end(), 0, bit_xor<>());
    }
};