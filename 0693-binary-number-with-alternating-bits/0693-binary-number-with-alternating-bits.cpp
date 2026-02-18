class Solution {
public:
    bool hasAlternatingBits(unsigned n) {
        bitset<32> B(n);
        int mB=31-countl_zero(n);
        bool prevB=1;
        for(int i=mB-1; i>=0; i--, prevB=!prevB){
            if (B[i]==prevB) return 0;
        }
        return 1;
    }
};